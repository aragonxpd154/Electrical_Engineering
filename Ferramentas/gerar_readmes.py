#!/usr/bin/env python3
"""
Gera os README.md do repositório a partir de Ferramentas/curriculo.json.

Uso (na raiz do repositório):
    python3 Ferramentas/gerar_readmes.py

Para atualizar a situação de uma disciplina (ex.: "Cursando" -> "Aprovado"),
edite o campo "situacao" em curriculo.json e rode o script de novo.
Situações aceitas: Aprovado, Dispensado, Cursando, A cursar.
"""
import json
import os
import re
from collections import defaultdict
from urllib.parse import quote

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DADOS = json.load(open(os.path.join(RAIZ, "Ferramentas", "curriculo.json"), encoding="utf-8"))

ICONE = {"Aprovado": "✅", "Dispensado": "☑️", "Cursando": "🟡", "A cursar": "⬜"}
CONCLUIDA = {"Aprovado", "Dispensado"}


def link(caminho_relativo):
    """Codifica espaços e acentos para links Markdown funcionarem no GitHub."""
    return quote(caminho_relativo, safe="/._-")


def titulo_livro(arquivo):
    return os.path.splitext(os.path.basename(arquivo))[0]


def conta_questoes(pasta):
    arq = os.path.join(RAIZ, pasta, "Exercicios.md")
    if not os.path.exists(arq):
        return 0
    texto = open(arq, encoding="utf-8").read()
    # cada questão tem exatamente um bloco de gabarito recolhível
    return len(re.findall(r"^<details>", texto, flags=re.M))


def arquivo_atividade(pasta):
    for nome in ("Exercicios.md", "Guia.md"):
        if os.path.exists(os.path.join(RAIZ, pasta, nome)):
            return nome
    return None


def readme_disciplina(d, complementar=False):
    pasta = d["pasta"]
    prof = "../../"
    linhas = [f"# {d['nome']}", ""]
    if complementar:
        linhas.append("**Trilha complementar** (fora da grade obrigatória)")
    else:
        linhas.append(f"**{d['periodo']}º período** · **{d['ch']} h** · **Situação:** {ICONE[d['situacao']]} {d['situacao']}")
    linhas += ["", f"[← Voltar à grade curricular]({prof}README.md)", ""]

    linhas += ["## Tópicos de estudo", ""] + [f"- {t}" for t in d["topicos"]] + [""]

    atividade = arquivo_atividade(pasta)
    linhas += ["## Exercícios e atividades", ""]
    if atividade == "Exercicios.md":
        n = conta_questoes(pasta)
        linhas.append(f"- 📝 [Lista de exercícios com gabarito](Exercicios.md) — {n} questões organizadas por tópico (gabarito recolhível em cada questão)")
    elif atividade == "Guia.md":
        linhas.append("- 🧭 [Guia e checklist da atividade](Guia.md)")
    for leg in d["legado"]:
        linhas.append(f"- 📂 [Listas, provas e trabalhos antigos]({link(leg['pasta'])}/) (origem: `{leg['origem']}`)")
    linhas.append("")

    if d["livros"] or d["solucoes"]:
        linhas += ["## Bibliografia disponível no repositório", ""]
        for l in d["livros"]:
            linhas.append(f"- 📘 [{titulo_livro(l)}]({prof}{link(l)})")
        for s in d["solucoes"]:
            linhas.append(f"- 🔑 [{titulo_livro(s)}]({prof}{link(s)})")
        linhas.append("")

    linhas += ["---", "*Arquivo gerado por `Ferramentas/gerar_readmes.py` a partir de `Ferramentas/curriculo.json`.*", ""]
    with open(os.path.join(RAIZ, pasta, "README.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(linhas))


def readme_bibliografia(todas):
    usos = defaultdict(list)
    for d in todas:
        for arq in d["livros"] + d["solucoes"]:
            usos[os.path.basename(arq)].append(d)

    def tabela(sub):
        pasta = os.path.join(RAIZ, "Bibliografia", sub)
        out = ["| Arquivo | Usado em |", "|---|---|"]
        for arq in sorted(os.listdir(pasta), key=str.lower):
            discs = ", ".join(f"[{x['nome']}](../{link(x['pasta'])}/)" for x in usos.get(arq, [])) or "—"
            out.append(f"| [{titulo_livro(arq)}]({link(sub + '/' + arq)}) | {discs} |")
        return out

    linhas = ["# Bibliografia", "", "[← Voltar à grade curricular](../README.md)", "",
              "Livros e solucionários herdados do repositório original, com indicação de em quais disciplinas da grade cada um é usado.", "",
              "## Livros", ""] + tabela("Livros") + ["", "## Solucionários", ""] + tabela("Solutions") + [""]
    with open(os.path.join(RAIZ, "Bibliografia", "README.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(linhas))


def readme_raiz():
    discs = DADOS["disciplinas"]
    ch_total = sum(d["ch"] for d in discs)
    ch_ok = sum(d["ch"] for d in discs if d["situacao"] in CONCLUIDA)
    n_ok = sum(1 for d in discs if d["situacao"] in CONCLUIDA)
    n_cur = sum(1 for d in discs if d["situacao"] == "Cursando")
    pct = round(100 * ch_ok / ch_total)
    barra = "█" * (pct // 5) + "░" * (20 - pct // 5)
    n_q = sum(conta_questoes(d["pasta"]) for d in discs + DADOS["complementares"])

    L = []
    L += ["# ⚡ Engenharia Elétrica — UVV", "",
          "Repositório de estudos organizado pela **grade curricular de Engenharia Elétrica da UVV** (Universidade Vila Velha), "
          "com listas de exercícios autorais e gabaritos por disciplina, material de apoio, bibliografia e trilhas extras.", "",
          "> Fork de [WeriksonAlves/Electrical_Engineering](https://github.com/WeriksonAlves/Electrical_Engineering). "
          "O material original (listas, provas, relatórios e livros da UFV) foi preservado e redistribuído nas pastas `Materiais/` "
          "de cada disciplina equivalente. Créditos do acervo original ao autor do repositório de origem.", "",
          "## 📊 Progresso", "",
          f"`{barra}` **{pct}%** da carga horária ({ch_ok} h de {ch_total} h) · "
          f"{n_ok} disciplinas concluídas · {n_cur} em curso · **{n_q} exercícios com gabarito**", "",
          "Legenda: ✅ Aprovado · ☑️ Dispensado · 🟡 Cursando · ⬜ A cursar", ""]

    L += ["## 🗂️ Grade curricular", ""]
    for p in range(1, 11):
        L += [f"### {p}º período", "", "| Disciplina | CH | Situação | Exercícios | Material antigo |", "|---|:-:|:-:|:-:|:-:|"]
        for d in [x for x in discs if x["periodo"] == p]:
            at = arquivo_atividade(d["pasta"])
            if at == "Exercicios.md":
                ex = f"[{conta_questoes(d['pasta'])} questões]({link(d['pasta'])}/Exercicios.md)"
            elif at == "Guia.md":
                ex = f"[guia]({link(d['pasta'])}/Guia.md)"
            else:
                ex = "—"
            leg = "📂" if d["legado"] else "—"
            L.append(f"| [{d['nome']}]({link(d['pasta'])}/) | {d['ch']} h | {ICONE[d['situacao']]} | {ex} | {leg} |")
        L.append("")

    L += ["## ➕ Trilhas complementares", "", "Conteúdos fora da grade que agregam à formação (ou material antigo sem disciplina equivalente).", "",
          "| Trilha | Exercícios | Material antigo |", "|---|:-:|:-:|"]
    for d in DADOS["complementares"]:
        ex = f"[{conta_questoes(d['pasta'])} questões]({link(d['pasta'])}/Exercicios.md)" if arquivo_atividade(d["pasta"]) else "—"
        L.append(f"| [{d['nome']}]({link(d['pasta'])}/) | {ex} | {'📂' if d['legado'] else '—'} |")
    L.append("")

    L += ["## 🧭 Como o repositório está organizado", "", "```text",
          "NN_Periodo/",
          "└── NN_Disciplina/",
          "    ├── README.md        → tópicos, situação, links para livros e material",
          "    ├── Exercicios.md    → lista autoral por tópico, com gabarito recolhível",
          "    ├── Guia.md          → (Estágio, TCC, Optativa, Atividades Complementares)",
          "    └── Materiais/       → listas, provas, relatórios e trabalhos do acervo original",
          "Complementares/         → trilhas extras (Telecom e Radiodifusão, Cálculo Numérico, ...)",
          "Bibliografia/           → livros e solucionários (índice em Bibliografia/README.md)",
          "Softwares/              → instaladores e manuais (FEMM, PLECS, WinPlot)",
          "Ferramentas/            → curriculo.json + script que gera estes READMEs",
          "```", "",
          "**Como estudar com as listas:** leia os tópicos no README da disciplina, resolva cada questão no papel e só então clique em **Gabarito** "
          "(as respostas ficam escondidas em blocos recolhíveis). As questões numéricas foram conferidas em Python; várias trazem o script de verificação.", "",
          "**Atualizar a situação de uma disciplina:** edite `situacao` em [`Ferramentas/curriculo.json`](Ferramentas/curriculo.json) e rode:", "",
          "```bash", "python3 Ferramentas/gerar_readmes.py", "```", ""]

    L += ["## 🔁 De onde veio cada pasta antiga", "",
          "O repositório original era organizado por departamento da UFV. Mapeamento para a nova estrutura:", "",
          "| Pasta original | Nova localização |", "|---|---|"]
    for d in discs + DADOS["complementares"]:
        for leg in d["legado"]:
            L.append(f"| `{leg['origem']}` | [`{d['pasta']}/{leg['pasta']}`]({link(d['pasta'] + '/' + leg['pasta'])}/) |")
    L.append("")

    L += ["## 🛠️ Ferramentas gratuitas recomendadas", "",
          "| Área | Ferramentas |", "|---|---|",
          "| Circuitos e simulação | LTspice, Qucs-S, [Falstad Circuit Simulator](https://www.falstad.com/circuit/), PLECS (pasta `Softwares/`) |",
          "| Cálculo e controle | Python (NumPy, SciPy, `python-control`), GNU Octave, Jupyter |",
          "| Eletromagnetismo | FEMM (pasta `Softwares/`) |",
          "| Desenho técnico e esquemas | LibreCAD, FreeCAD, QElectroTech, KiCad, draw.io |",
          "| Digital e embarcados | Logisim-evolution, Icarus Verilog + GTKWave, PlatformIO, Arduino IDE |", ""]

    L += ["---", "*README gerado por [`Ferramentas/gerar_readmes.py`](Ferramentas/gerar_readmes.py). Mantido por [aragonxpd154](https://github.com/aragonxpd154).*", ""]
    with open(os.path.join(RAIZ, "README.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(L))


if __name__ == "__main__":
    for d in DADOS["disciplinas"]:
        readme_disciplina(d)
    for d in DADOS["complementares"]:
        readme_disciplina(d, complementar=True)
    readme_bibliografia(DADOS["disciplinas"] + DADOS["complementares"])
    readme_raiz()
    print("READMEs gerados.")
