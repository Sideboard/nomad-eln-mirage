from nomad.config.models.plugins import SchemaPackageEntryPoint
from pydantic import Field


class ELNMirageEntryPoint(SchemaPackageEntryPoint):
    parameter: int = Field(0, description='Custom configuration parameter')

    def load(self):
        from nomad_eln_mirage.schema_packages.eln_mirage import m_package

        return m_package


eln_mirage = ELNMirageEntryPoint(
    name='ELN Mirage',
    description='Exemplatory schema plugin for testing ELNs',
)
