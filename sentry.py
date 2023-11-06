import logging

# Obtenez une instance du logger du module actuel
logger = logging.getLogger(__name__)

# Utilisez le logger pour enregistrer des messages
logger.debug("Ceci est un message de débogage")
logger.info("Ceci est un message d'information")
logger.warning("Ceci est un message d'avertissement")
logger.error("Ceci est un message d'erreur")


def fonction_critique():
    try:
        x = 100 / 0
    except ZeroDivisionError as e:
        # Enregistrez l'erreur dans les journaux avec le niveau approprié
        logger.error("Une erreur critique s'est produite : %s", str(e))
