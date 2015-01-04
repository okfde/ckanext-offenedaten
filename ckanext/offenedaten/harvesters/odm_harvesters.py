# -*- coding: utf-8 -*-
from ckanext.offenedaten.harvesters.odm_harvester import OdmHarvester
from odm.catalogs.portals.baden_wuerttemberg import BwReader
from odm.catalogs.portals.braunschweig import BraunschweigReader
from odm.catalogs.portals.bochum import BochumReader
from odm.catalogs.portals.diepholz import DiepholzReader
from odm.catalogs.portals.bremen import BremenReader
from odm.catalogs.portals.moers import MoersReader
from odm.catalogs.portals.rostock import RostockReader
from odm.catalogs.portals.rheinland_pfalz import RlpReader
from odm.catalogs.portals.ulm import UlmReader
from odm.catalogs.portals.ckanApiV3 import CkanReader


# Weired way of constructing a python class
def def_harvester(odm_reader):
    return type(odm_reader.info()['name'],
                (OdmHarvester,),
                {"scraper": odm_reader})


baden_wuerttemberg = def_harvester(BwReader())
bochum             = def_harvester(BochumReader())
braunschweig       = def_harvester(BraunschweigReader())
bremen             = def_harvester(BremenReader())
diepholz           = def_harvester(DiepholzReader())
moers              = def_harvester(MoersReader())
rheinland_pfalz    = def_harvester(RlpReader())
rostock            = def_harvester(RostockReader())
ulm                = def_harvester(UlmReader())
koeln              = def_harvester(CkanReader('koeln'))
bonn               = def_harvester(CkanReader('bonn'))
hamburg            = def_harvester(CkanReader('hamburg'))
frankfurt          = def_harvester(CkanReader('frankfurt'))
aachen             = def_harvester(CkanReader('aachen'))
berlin             = def_harvester(CkanReader('berlin'))
