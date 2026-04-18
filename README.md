# DevSecOps Project - API Flask vulnérable

## 📌 Description

Ce projet est une API Flask volontairement vulnérable, créée dans le cadre d'un projet DevSecOps. Il démontre l'intégration de contrôles de sécurité automatisés dans un pipeline CI/CD avec GitHub Actions, Trivy et Conftest.

## 🛠️ Technologies utilisées

| Outil | Usage |
|-------|-------|
| **Python / Flask** | Application web vulnérable |
| **Docker** | Conteneurisation de l'application |
| **GitHub Actions** | Pipeline CI/CD |
| **Trivy** | Scan de vulnérabilités (dépendances + image Docker) |
| **Conftest** | Policy as Code (vérification des pods Kubernetes) |
| **Yamllint** | Linting des fichiers YAML |

## 📁 Structure du projet
├── .github/workflows/
│ └── ci.yml # Pipeline CI/CD GitHub Actions
├── policy/
│ └── deny_root.rego # Politique Conftest (interdit les pods root)
├── app.py # API Flask vulnérable
├── requirements.txt # Dépendances Python (Flask 2.0.1 vulnérable)
├── Dockerfile # Image Docker basée sur Python 3.9-slim
├── deployment.yaml # Déploiement Kubernetes de test
└── README.md # Ce fichier

## 🚀 Pipeline CI/CD

Le pipeline GitHub Actions exécute 4 jobs :

| Job | Description |
|-----|-------------|
| `linting` | Vérifie la syntaxe des fichiers YAML avec yamllint |
| `build` | Construit l'image Docker |
| `security-scan` | Scanne les dépendances et l'image Docker avec Trivy |
| `policy-check` | Vérifie que les pods Kubernetes ne tournent pas en root (Conftest) |

## 🔍 Vulnérabilités détectées

### Scan des dépendances (Trivy fs)

| Bibliothèque | Vulnérabilité | Sévérité | Version | Version corrigée |
|--------------|---------------|----------|---------|------------------|
| Flask | CVE-2023-30861 | HIGH | 2.0.1 | 2.3.2 |

### Scan de l'image Docker (Trivy image)

| Bibliothèque | Vulnérabilité | Sévérité | Version | Version corrigée |
|--------------|---------------|----------|---------|------------------|
| openssl | CVE-2025-15467 | CRITICAL | 3.5.1 | 3.5.4 |
| libc-bin | CVE-2026-0861 | HIGH | 2.41-12 | 2.41-12+deb13u2 |

## 🛡️ Politique de sécurité (Conftest)

La politique `deny_root.rego` bloque tout déploiement Kubernetes dont les pods tournent en mode root :

    package main
    
    deny[msg] {
      input.kind == "Deployment"
      container := input.spec.template.spec.containers[_]
      not container.securityContext.runAsNonRoot == true
      msg = sprintf("❌ Le pod '%v' doit être configuré avec runAsNonRoot: true", [container.name])
    }

## 📝 Recommandations

  Mettre à jour Flask vers la version 2.3.2
   
   Utiliser une image de base plus récente (ex: python:3.12-slim)
   
   Activer le blocage des vulnérabilités CRITICAL (exit-code: '1')
   
   Ajouter Semgrep (SAST) pour analyser le code source
   
   Générer un SBOM avec Trivy
   ## 👨‍🏫 Enseignant

**Monsieur Laurent FREREBEAU**  
ESTIAM PARIS - DevSecOps - 5DVSC0PS - 2025/2026

## 👤 Auteur
Jamal Jabrane - Projet DevSecOps 

## 📅 Date
Avril 2026

## 📄 Licence
Ce projet est réalisé dans un cadre pédagogique.
