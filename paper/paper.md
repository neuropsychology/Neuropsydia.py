---
title: 'Neuropsydia.py: A Python Module for Creating Experiments, Tasks and Questionnaires'
tags:
  - python
  - psychology
  - questionnaire
  - experiments
  - neuropsychology
  - tasks
  - assessment
authors:
 - name: Dominique Makowski
   orcid: 0000-0001-5375-9967
   affiliation: 1, 2
 - name: Léo Dutriaux
   affiliation: 1, 2
affiliations:
 - name: Memory and Cognition Lab', Institute of Psychology, University of Sorbonne Paris Cité, France
   index: 1
 - name: INSERM U894, Center for Psychiatry and Neuroscience, Paris, France
date: 03 April 2017
bibliography: paper.bib
---

# Summary

Introduction. La neuropsychologie comporte deux aspects intimement liés : la recherche expérimentale, ainsi que la clinique. Cependant, l’écart entre la recherche et la clinique n’a cessé de grandir depuis l’informatisation des procédures au cours de la dernière décennie. En effet, les hôpitaux et les cliniciens libéraux sont souvent sous-équipés en termes de software et hardware récent. De plus, les quelques entreprises privées développant et validant des outils présentent certains inconvénients, dont un prix souvent important, excluant les clients individuels et les institutions trop petites ou issues de pays en développement. De plus, ces programmes nécessitent souvent une installation fastidieuse, sont non-portable et non-évolutifs. Pour pallier ces manques et augmenter la précision des mesures par rapport à des tests papiers, nous présentons le développement d’une solution gratuite, open-source, évolutive, ouverte et portable, permettant aux neuropsychologues de se centrer sur l’interprétation et la réflexion plutôt que sur la passation et la cotation des tests.

Méthodologie. Basé sur Python, un langage open-source, nous avons développé un logiciel portable (sur clé USB), ne nécessite aucune installation, adapté à des ordinateurs anciens, permettant 1) la réalisation facile et rapide de nouveaux tests et questionnaires informatisés (ne nécessitant quasiment aucune connaissances de programmation) et 2) intégrant un canevas d’anamnèse complet, un questionnaire de personnalité et de régulation émotionnelle traduits et en cours de validation, ainsi que des tâches originales mesurant la flexibilité, la mémoire de travail et le contrôle cognitif dans ses conceptualisations les plus récentes. Le stockage des données est transparent et adapté aussi bien à la recherche qu’à la clinique (enregistrement exhaustif et résumé). De plus, le logiciel extrait automatiquement les scores ainsi que de nouveaux indices complexes par calcul statistique, et les compare automatiquement à une base de données, produisant un compte-rendu sous forme de document Word où sont présentés les graphiques, commentaires et analyses des scores du sujet par rapport à la population parente. 

Conclusion. Enfin, ce logiciel est en constante évolution : de nombreux tests sont en cours de création et de validation, et un agrandissement de la base de données comprenant la population parente est également en cours. L’état d’avancement du projet sera présenté.



Pyhector is a Python interface for the simple climate model Hector (Hartin et al. 2015) developed in C++. Simple climate models like Hector can, for instance, be used in the analysis of scenarios within integrated assessment models like GCAM1, in the emulation of complex climate models, and in uncertainty analyses.

Hector is an open-source, object oriented, simple global climate carbon cycle model. Its carbon cycle consists of a one pool atmosphere, three terrestrial pools which can be broken down into finer biomes or regions, and four carbon pools in the ocean component. The terrestrial carbon cycle includes primary production and respiration fluxes. The ocean carbon cycle circulates carbon via a simplified thermohaline circulation, calculating air-sea fluxes as well as the marine carbonate system (Hartin et al. 2016).

The model input is time series of greenhouse gas emissions; as example scenarios for these the Pyhector package contains the Representative Concentration Pathways (RCPs)2. These were developed to cover the range of baseline and mitigation emissions scenarios and are widely used in climate change research and model intercomparison projects. Using DataFrames from the Python library Pandas (McKinney 2010) as a data structure for the scenarios simplifies generating and adapting scenarios. Other parameters of the Hector model can easily be modified when running the model.

Neuropsydia.py can be installed using pip from the Python Package Index^[<https://pypi.python.org/pypi/neuropsydia>]. Source code and issue tracker are available in Neuropsydia.py's GitHub repository^[<https://github.com/neuropsychology/Neuropsydia.py>]. Documentation, tutorials and examples are provided through Readthedocs^[<http://neuropsydia.readthedocs.io/en/latest/>]. Usage examples and a test script are also contained in the repository^[<https://github.com/neuropsychology/Neuropsydia.py/tree/master/examples>], ^[<https://github.com/neuropsychology/Neuropsydia.py/tree/master/tests>].

# References