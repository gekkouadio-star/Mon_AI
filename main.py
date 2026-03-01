import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import httpx
from datetime import datetime
import random
import os
from dotenv import load_dotenv

load_dotenv()

 
app = FastAPI()
 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
 
# --- CONFIGURATION ---
API_KEY = os.getenv("API_KEY")

URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={API_KEY}"
 
class ChatRequest(BaseModel):
    message: str
    sessionId: str
 
# ======================================================
# PROFIL OFFICIEL
# ======================================================
PROFILE_TEXT = """
Gérard KOUADIO est Data Engineer, Data Analyst, Data Scientist
et Analyste Risques de Crédit basé en Île-de-France (Paris).

Formation :
- Master Big Data, Data Science et Analyse des Risques (Université de Montpellier)
- Master 2 Monnaie, Banque, Finance, Assurance (Université de Limoges)

Expertise Data :
- Extraction et manipulation SQL
- PySpark et pipelines de données
- Détection d’anomalies (LSTM)
- Modélisation XGBoost
- Streamlit et Power BI
- Docker, Dataiku, GitHub

Expertise Banque & Risques :
- Analyse financière
- Conformité KYC / LCB-FT
- Réglementation Bâle I, II, III
- Gestion des risques de crédit

Expériences :
- Projet Data : traitement des données, détection d’anomalies, visualisation, modélisation et prédiction via le web apps data
- Banque Populaire : Chargé de clientèle en agence
- BNP Paribas : Assistant Chargé d’Affaires Professionnels

Certifications :
- Certification AMF
- Certifications Dataiku (MLOps, ML, Generative AI, etc)

Langues :
- Français (maternel)
- Anglais (intermédiaire)

Contact :
- gekkouadio@gmail.com
- +33650342806
"""

# ======================================================
# QUESTIONS ENTRETIEN DATA
# ======================================================
INTERVIEW_QA = """

1. Présente ton profil Big Data
Je suis Data Engineer orienté sur la conception, la construction, la mise en œuvre et le support des systèmes permettant de collecter, stocker, traiter et analyser de grands volumes de données. Je travaille sur l’analyse de données massives, la détection d’anomalies et la mise en production de modèles de machine learning.

2. Quelle est ton expérience avec les données massives ?
J’ai travaillé sur des séries temporelles contenant plus d’un million de lignes et plus de 70 variables. J’ai réalisé l’exploration, la préparation des données, la visualisation, la modélisation et la prédiction pour détecter les anomalies.

3. Quels outils Big Data maîtrises-tu ?
Python, Numpy, Pandas, PySpark, SQL, NoSQL, Talend, Docker, Dataiku, GitHub, Streamlit et Power BI.

4. Comment détectes-tu des anomalies dans les données ?
Je prépare les données, j’explore les tendances, puis j’utilise des modèles comme LSTM pour détecter les anomalies et XGBoost pour identifier les variables explicatives.

5. Comment garantis-tu la qualité des données ?
Je vérifie les valeurs manquantes, les incohérences, les doublons et les valeurs aberrantes avant toute modélisation.

6. Comment expliques-tu tes résultats à un métier non technique ?
Je simplifie les indicateurs clés, j’explique l’impact métier et je propose des recommandations concrètes pour améliorer la prise de décision.

7. Pourquoi veux-tu travailler dans la data ?
Parce que la data est au cœur de la prise de décision et permet d’anticiper les risques, détecter les anomalies et optimiser la performance d’une entreprise. C’est un domaine en constante évolution qui me passionne.

8. Quelle est ta valeur ajoutée comme profil junior ?
Ma rigueur analytique, ma capacité d’apprentissage rapide et ma maîtrise d’outils modernes de data engineering, data analysis, machine learning et détection de fraudes.

### QUESTIONS-RÉPONSES SPÉCIALISÉES (DATA & BANQUE/RISQUE)

9. Comment la Data Science aide-t-elle à la gestion des risques de crédit ? 
Elle permet de construire des modèles de Credit Scoring plus précis, comme ceux utilisant XGBoost, pour prédire la probabilité de défaut.

10. Pourquoi as-tu utilisé un modèle LSTM pour ton projet sur les moteurs ? 
Les réseaux LSTM mémorisent les dépendances à long terme dans les séries temporelles, une logique identique à l'analyse de l'évolution des flux financiers ou des cours de bourse.

11. Quel est le lien entre l'économétrie et le Machine Learning dans ton parcours ? 
L'économétrie m'apporte la rigueur statistique, tandis que le Machine Learning me permet d'automatiser les prédictions sur des volumes de données massifs.

12. Sais-tu modéliser la détection de fraudes ? 
Oui, j'étudie l'identification de comportements atypiques (anomalies) via le Deep Learning dans mon Master à Montpellier.

13. Comment interprètes-tu les résultats d'un modèle pour un décideur bancaire ? 
J'utilise des Web Apps comme Streamlit ou des dashboards Power BI pour rendre les modèles complexes transparents et actionnables pour les gestionnaires de risques.

14. Pourquoi un Data Engineer est-il crucial pour la conformité LCB-FT ? 
Il faut des pipelines ETL robustes pour croiser en temps réel les transactions avec les listes de sanctions sans perte de données.

15. Quelle est l'utilité de SQL et DBeaver dans ton expérience bancaire ? 
Cela me permet d'extraire des données du Back-Office bancaire pour effectuer des audits de conformité ou des analyses de portefeuille.

16. As-tu déjà travaillé avec des données de marchés financiers ? 
Oui, mon Master 2 couvrait les actions et produits de taux, que je sais traiter avec Pandas et Numpy.

17. Comment Docker et DevOps s'appliquent-ils au secteur financier ? 
Ils garantissent que les modèles de risque sont déployés dans des environnements sécurisés, isolés et reproductibles, essentiels pour les audits réglementaires.

18. Quelle est ta maîtrise du Big Data (PySpark) pour la banque ? 
J'utilise PySpark pour traiter des millions de lignes de transactions là où les outils classiques atteignent leurs limites.

19. Connais-tu les accords de Bâle III ? 
Oui, je comprends les exigences de fonds propres et les ratios de liquidité que les banques doivent monitorer grâce à la donnée.

20. Quel est le lien entre le KYC et la Data ? 
Le KYC génère des données textuelles massives. J'utilise le Text Mining pour automatiser l'analyse de conformité des dossiers.

21. Comment l'analyse financière s'intègre-t-elle à tes compétences Data ? 
Je peux automatiser l'analyse des bilans via Python pour calculer instantanément les ratios de solvabilité d'une entreprise.

22. Qu'est-ce que la détection d'anomalies apporte au Back-Office ? 
Elle permet de repérer automatiquement des erreurs de saisie ou des opérations suspectes dans les systèmes informatiques internes.

23. Sais-tu utiliser VBA pour la finance ? 
Oui, je maîtrise VBA pour automatiser des reportings financiers ou des outils de calcul de risque sous Excel.

24. Data Analyst ou Analyste Risque : comment te définis-tu ? 
Je suis un profil hybride : j'ai la vision métier pour comprendre le risque bancaire et la compétence technique pour le modéliser.

25. Quelles sont tes certifications pertinentes pour la banque ? 
Je possède la certification AMF (Mai 2025) et 6 certifications Dataiku MLOps.

26. Comment garantis-tu la qualité des données dans un projet financier ? 
Par des étapes de nettoyage rigoureuses (Data Cleaning) sous Python et une vérification de conformité dès l'entrée des dossiers.

27. Pourquoi le cloud (Azure DevOps) est-il important pour un analyste risques ? 
Il permet une collaboration agile pour mettre à jour les modèles de notation en continu.

28. Quel est l'avantage de Python par rapport aux outils bancaires classiques ? 
Python offre une flexibilité totale, permettant de passer de l'extraction SQL à la visualisation et au Deep Learning dans un seul flux.
"""

# ======================================================
# REGLES LLM
# ======================================================
ASSISTANT_RULES = """

Répondre clairement et directement.
Pas de présentation automatique.
Répondre uniquement à la question.
Si inconnu : dis lui qu'il reformule la question autrement stp.
"""

# ======================================================
# CONVERSATION NATURELLE
# ======================================================
GREETINGS = ["bonjour","salut","hello","bonsoir","hey","coucou"]
THANKS = ["merci","merci beaucoup","thanks"]
HOW_ARE_YOU = ["tu vas bien","ça va","comment vas tu","comment ça va"]

GREETING_RESPONSES = [
    "Bonjour, comment puis-je vous aider ?",
    "Bonjour, que souhaitez-vous savoir ?",
    "Bonjour, je vous écoute."
]

THANKS_RESPONSES = [
    "Avec plaisir.",
    "Je vous en prie.",
    "N'hésitez pas si besoin."
]

HOW_RESPONSES = [
    "Je vais bien, merci. Et vous ?",
    "Très bien merci. Comment puis-je vous aider ?",
    "Tout va bien, merci."
]

# ======================================================
# QUESTIONS OUVERTES GENERALES
# ======================================================
OPEN_QUESTIONS = {
    
    # -----------------------------
    # IDENTITE / ROLE
    # -----------------------------
    "qui es tu": "Je peux fournir des informations sur le profil, les compétences, les projets data et la carrière professionnelle de Gérard KOUADIO.",
    "parle moi de toi": "Gérard KOUADIO est un professionnel de la data spécialisé dans le traitement de données massives, le machine learning et l’analyse des risques.",
    "explique ton profil": "Profil data complet combinant data engineering, analyse de données et modélisation prédictive appliquée aux risques et à la performance.",

    # -----------------------------
    # CAPACITES ASSISTANT
    # -----------------------------
    "que peux tu faire": "Je peux répondre aux questions sur son profil data, ses compétences techniques, ses expériences, ses projets et simuler des réponses d’entretien.",
    "comment peux tu m'aider": "Je peux expliquer ses compétences, détailler ses projets, préparer un entretien, ou répondre à des questions techniques liées à la data.",
    "comment tu fonctionnes": "Je réponds aux questions simples directement et j’utilise l’intelligence artificielle pour les questions complexes liées au profil ou à la data.",
    "tu peux m'aider": "Oui, dites-moi simplement ce dont vous avez besoin.",

    # -----------------------------
    # COMPETENCES / EXPERTISE
    # -----------------------------
    "quelles sont tes compétences": "Ses compétences couvrent Python, SQL, PySpark, machine learning, détection d’anomalies, visualisation de données et gestion des risques.",
    "dans quoi es tu specialise": "Il est spécialisé dans le data engineering, l’analyse de données massives et la modélisation prédictive.",
    "quels sont tes points forts": "Analyse de données massives, détection d’anomalies, modélisation machine learning et gestion des risques.",

    # -----------------------------
    # OBJECTIFS / CARRIERE
    # -----------------------------
    "quel est ton objectif": "Développer une expertise avancée en data engineering et analyse prédictive appliquée aux systèmes complexes et à la gestion des risques.",
    "quel est ton projet professionnel": "Évoluer vers des projets data à forte valeur ajoutée combinant big data, intelligence artificielle et analyse des risques.",
    "quel sont tes ambitions": "Approfondir l’expertise en data engineering et en modélisation avancée pour résoudre des problématiques complexes.",

    # -----------------------------
    # DATA / IA GENERAL
    # -----------------------------
    "qu'est-ce la data ou explique la data": "La data correspond aux informations collectées, stockées et analysées pour comprendre des phénomènes et prendre des décisions.",
    "explique le big data": "Le big data désigne le traitement et l’analyse de très grands volumes de données difficiles à gérer avec les outils classiques.",
    "explique le machine learning": "Le machine learning est une méthode qui permet aux systèmes informatiques d’apprendre automatiquement à partir des données.",
    "explique l'intelligence artificielle": "L’intelligence artificielle regroupe les techniques permettant aux machines d’imiter certaines capacités humaines comme l’apprentissage ou la prise de décision.",

    # -----------------------------
    # CONSEILS GENERAUX
    # -----------------------------
    "comment apprendre la data": "Il est conseillé de commencer par Python, les statistiques, puis le machine learning et enfin les outils big data.",
    "comment devenir data engineer": "Il faut maîtriser la programmation, les bases de données, les pipelines de données et le traitement distribué.",
    "conseil pour entretien data": "Bien comprendre les bases techniques, expliquer ses projets clairement et démontrer sa capacité à résoudre des problèmes.",
    "comment reussir un entretien": "Préparer ses expériences, illustrer ses compétences avec des exemples concrets et rester structuré dans ses réponses.",

    # -----------------------------
    # AIDE GENERALE
    # -----------------------------
    "aide moi": "Bien sûr. Que souhaitez-vous savoir exactement ?",
    "j'ai une question": "Je vous écoute.",
    "je veux apprendre": "Très bien. Sur quel sujet souhaitez-vous apprendre davantage ?",
    "explique moi": "Que souhaitez-vous que j’explique précisément ?",

    # -----------------------------
    # DEMANDES DE PRECISION
    # -----------------------------
    "je ne comprends pas": "D’accord. Quelle partie souhaitez-vous que je reformule ou détaille ?",
    "peux tu préciser": "Bien sûr. Que voulez-vous que je précise exactement ?",
    "tu peux détailler": "Avec plaisir. Quel point souhaitez-vous approfondir ?",
    "c'est pas clair": "Merci de me le dire. Que souhaitez-vous que je reformule ?",

    # -----------------------------
    # DEMANDES D’EXEMPLES
    # -----------------------------
    "donne moi un exemple": "Bien sûr. Sur quel sujet voulez-vous un exemple ?",
    "as tu un exemple concret": "Oui. Quel domaine vous intéresse ?",
    "montre moi comment faire": "D’accord. Que voulez-vous apprendre à faire précisément ?",

    # -----------------------------
    # DEMANDES D’ASSISTANCE
    # -----------------------------
    "tu peux m'aider": "Bien sûr. Dites-moi ce dont vous avez besoin.",
    "j'ai besoin d'aide": "Je suis là pour vous aider. Quel est votre besoin ?",
    "guide moi": "Avec plaisir. Sur quoi souhaitez-vous être guidé ?",
    "accompagne moi": "Très bien. Dans quelle tâche avez-vous besoin d’accompagnement ?",

    # -----------------------------
    # DEMANDES D’APPRENTISSAGE
    # -----------------------------
    "apprends moi": "Très bien. Quel sujet souhaitez-vous apprendre ?",
    "forme moi": "Avec plaisir. Dans quel domaine voulez-vous vous former ?",
    "je débute": "Bienvenue. Sur quel sujet souhaitez-vous commencer ?",

    # -----------------------------
    # VERIFICATION / CONFIRMATION
    # -----------------------------
    "est ce que c'est correct": "Pouvez-vous préciser ce que vous souhaitez vérifier ?",
    "tu es sûr": "Souhaitez-vous que je vérifie une information en particulier ?",
    "confirme moi": "Que souhaitez-vous que je confirme exactement ?",

    # -----------------------------
    # AUTRES DEMANDES COURANTES
    # -----------------------------
    "que peux tu faire": "Je peux répondre à vos questions, expliquer des concepts, vous aider à apprendre ou résoudre un problème. Que souhaitez-vous faire ?",
    "comment ça marche": "Que souhaitez-vous comprendre sur le fonctionnement ?",
    "par où commencer": "Tout dépend de votre objectif. Que souhaitez-vous apprendre ou faire ?"
    }

# ======================================================
# DETECTION INTENTION
# ======================================================
def contains(text, patterns):
    return any(p in text for p in patterns)

# ======================================================
# ROUTE PRINCIPALE
# ======================================================
@app.post("/chat")
async def chat(request: ChatRequest):

    msg = request.message.lower().strip()

    # ----- SALUTATION -----
    if contains(msg, GREETINGS):
        return {"reply": random.choice(GREETING_RESPONSES)}

    # ----- MERCI -----
    if contains(msg, THANKS):
        return {"reply": random.choice(THANKS_RESPONSES)}

    # ----- ETAT -----
    if contains(msg, HOW_ARE_YOU):
        return {"reply": random.choice(HOW_RESPONSES)}

    # ----- HEURE -----
    if "heure" in msg:
        return {"reply": f"Il est actuellement {datetime.now().strftime('%H:%M')}."}

    # ----- QUESTIONS OUVERTES -----
    for key, value in OPEN_QUESTIONS.items():
        if key in msg:
            return {"reply": value}

    # ----- LLM POUR QUESTIONS COMPLEXES -----
    prompt = (
        f"{ASSISTANT_RULES}\n\n"
        f"PROFIL : {PROFILE_TEXT}\n\n"
        f"ENTRETIEN : {INTERVIEW_QA}\n\n"
        f"QUESTION : {request.message}"
    )

    payload = {"contents": [{"parts": [{"text": prompt}]}]}

    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(URL, json=payload, timeout=30.0)
            data = response.json()

            if response.status_code != 200:
                error_msg = data.get('error', {}).get('message', 'Erreur inconnue')
                return {"reply": f"Erreur Google ({response.status_code}) : {error_msg}"}

            if "candidates" in data and data["candidates"]:
                reply = data["candidates"][0]["content"]["parts"][0]["text"].strip()
                return {"reply": reply}

            return {"reply": "Je n'ai pas pu générer de réponse."}

        except Exception as e:
            return {"reply": f"Erreur de connexion : {str(e)}"}
 
if __name__ == "__main__":
    import os
    import uvicorn

    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
 
