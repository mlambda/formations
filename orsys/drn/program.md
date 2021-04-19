# Deep Learning et réseaux de neurones, les fondamentaux

## Durée

3 jours.

## Prix 2021

2750 € H.T.

## Participants

Ingénieurs, Data Scientists désirant s'initier aux réseaux de neurones et au Deep Learning.

## Prérequis

Avoir des bases en programmation. Avoir une bonne maîtrise des outils informatiques et des statistiques.

## Objectifs pédagogiques

- Comprendre les clés fondamentales d'une approche Machine ou Deep Learning
- Maîtriser les bases théoriques et pratiques d'architecture et de convergence de réseaux de neurones
- Connaître les différentes architectures fondamentales existantes et maîtriser leurs implémentations fondamentales
- Maîtriser les méthodologies de mise en place de réseaux de neurones, les points forts et les limites de ces outils

## Méthodes pédagogiques

Ce séminaire se base sur des présentations, des échanges et des études de cas. Des outils comme Lasagne ou Keras seront présentés.

## Description

L'Intelligence Artificielle a bouleversé de nombreux domaines scientifiques et révolutionné un grand nombre de secteurs économiques. Néanmoins, sa présentation dans les grands médias relève souvent du fantasme, très éloignée de ce que sont réellement les domaines du Machine Learning ou du Deep Learning. Ce séminaire vous permettra de maîtriser les concepts clé du Deep Learning et de ses différents domaines de spécialisation. Vous découvrirez également les principales architectures de réseau existant aujourd'hui.

## Programme

### Introduction IA, Machine Learning et Deep Learning

- Historique, concepts de base et applications de l'intelligence artificielle loin des fantasmes portés par ce domaine.
- Intelligence collective : agréger une connaissance partagée par de nombreux agents virtuels.
- Algorithmes génétiques : faire évoluer une population d'agents virtuels par sélection.
- Machine Learning usuel : définition.
- Types de tâches : Supervised Learning, Unsupervised Learning, Reinforcement Learning.
- Types d'actions : classification, régression, clustering, estimation de densité, réduction de dimensionalité.
- Exemples d'algorithmes Machine Learning : régression linéaire, Naive Bayes, Random Tree.
- Machine Learning versus Deep Learning : pourquoi le ML reste aujourd'hui l'état de l'art (Random Forests & XGBoosts) ?

### Concepts fondamentaux d'un réseau de neurones

- Rappel de bases mathématiques.
- Le réseau de neurones : architecture, fonctions d'activation et de pondération des activations précédentes...
- L'apprentissage d'un réseau de neurones : fonctions de coût, back-propagation, stochastic gradient descent...
- Modélisation d'un réseau de neurones : modélisation des données d'entrée et de sortie selon le type de problème.
- Approximer une fonction par un réseau de neurones. Approximer une distribution par un réseau de neurones.
- Data Augmentation : comment équilibrer un dataset ?
- Généralisation des résultats d'un réseau de neurones.
- Initialisations et régularisations d'un réseau de neurones : L1/L2 Regularization, Batch Normalization.
- Optimisations et algorithmes de convergence.

#### Démonstration

Approximation d'une fonction et d'une distribution par un réseau de neurones.

### Outils usuels Machine Learning et Deep Learning

- Outils de gestion de donnée : Apache Spark, Apache Hadoop.
- Outils Machine Learning usuel : Numpy, Scipy, Sci-kit.
- Frameworks DL haut niveau : PyTorch, Keras, Lasagne.
- Frameworks DL bas niveau : Theano, Torch, Caffe, Tensorflow.

#### Démonstration

Applications et limites des outils présentés.

### Convolutional Neural Networks (CNN)

- Présentation des CNNs : principes fondamentaux et applications.
- Fonctionnement fondamental d'un CNN : couche convolutionnelle, utilisation d'un kernel, padding et stride...
- Architectures CNN ayant porté l'état de l'art en classification d'images : LeNet, VGG Networks, Network in Network...
- Utilisation d'un modèle d'attention.
- Application à un cas de figure de classification usuel (texte ou image).
- CNNs pour la génération : super-résolution, segmentation pixel à pixel.
- Principales stratégies d'augmentation des Feature Maps pour la génération d'une image.

#### Étude de cas

Innovations apportées par chaque architecture CNN et leurs applications plus globales (convolution 1x1 ou connexions résiduelles).

### Recurrent Neural Networks (RNN)

- Présentation des RNNs : principes fondamentaux et applications.
- Fonctionnement fondamental du RNN : hidden activation, back propagation through time, unfolded version.
- Évolutions vers les GRU (Gated Recurrent Units) et LSTM (Long Short Term Memory).
- Problèmes de convergence et vanising gradient.
- Types d'architectures classiques : prédiction d'une série temporelle, classification...
- Architecture de type RNN Encoder Decoder. Utilisation d'un modèle d'attention.
- Applications NLP : word/character encoding, traduction.
- Applications vidéo : prédiction de la prochaine image générée d'une séquence vidéo.

#### Démonstration

Différents états et évolutions apportées par les architectures Gated Recurrent Units et Long Short Term Memory.

### Modèles générationnels : VAE et GAN

- Présentation des modèles générationnels Variational AutoEncoder (VAE) et Generative Adversarial Networks (GAN).
- Auto-encoder : réduction de dimensionnalité et génération limitée.
- Variational AutoEncoder : modèle générationnel et approximation de la distribution d'une donnée.
- Définition et utilisation de l'espace latent. Reparameterization trick.
- Fondamentaux du Generative Adversarial Networks.
- Convergence d'un GAN et difficultés rencontrées.
- Convergence améliorée : Wasserstein GAN, BeGAN. Earth Moving Distance.
- Applications de génération d'images ou de photographies, génération de texte, super résolution.

#### Démonstration

Applications des modèles générationnels et utilisation de l'espace latent.

### Deep Reinforcement Learning

- Reinforcement Learning.
- Utilisation d'un réseau de neurones pour approximer la fonction d'état.
- Deep Q Learning : experience replay et application au contrôle d'un jeu vidéo.
- Optimisations de la politique d'apprentissage. On-policy et off-policy. Actor critic architecture. A3C.
- Applications : contrôle d'un jeu vidéo simple ou d'un système numérique.

#### Démonstration

Contrôle d'un agent dans un environnement défini par un état et des actions possibles.
