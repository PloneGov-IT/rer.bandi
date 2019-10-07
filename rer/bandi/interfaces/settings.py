from zope.interface import Interface
from zope import schema
from plone.app.registry.browser import controlpanel
from rer.bandi import bandiMessageFactory as _


class IBandoSettings(Interface):
    """
    Settings used for announcements default value
    """

    default_ente = schema.Tuple(
        title=_(u"default_ente"),
        required=False,
        value_type=schema.TextLine(),
        missing_value=None
    )

    default_destinatari = schema.Tuple(
        title=_(u"default_destinatari_bandi"),
        required=False,
        value_type=schema.TextLine(),
        missing_value=None
    )

    tipologie_bando = schema.Tuple(
        title=_(u"Announcement types"),
        description=_(u"These values will extend bandi.xml vocabulary on filesystem"),
        required=False,
        value_type=schema.TextLine(),
        missing_value=None
    )


class BandiSettings(controlpanel.RegistryEditForm):
    schema = IBandoSettings
    id = 'BandiSettings'
    label = u"Impostazioni per i bandi"


class BandiSettingsControlPanel(controlpanel.ControlPanelFormWrapper):

    form = BandiSettings
