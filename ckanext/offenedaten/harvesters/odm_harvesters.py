# -*- coding: utf-8 -*-
from ckanext.offenedaten.harvesters.odm_harvester import OdmHarvester
from odm.catalogs.portals.baden_wuerttemberg import BwReader
# from odm.catalogs.portals.braunschweig import BraunschweigReader
# from odm.catalogs.portals.bochum import BochumReader
# from odm.catalogs.portals.diepholz import DiepholzReader
# from odm.catalogs.portals.bremen import BremenReader
# from odm.catalogs.portals.koeln import KoelnReader
# from odm.catalogs.portals.moers import MoersReader
# from odm.catalogs.portals.rostock import RostockReader


# Weired way of constructing a python class
def def_harvester(odm_reader):
    return type(odm_reader.info()['name'],
                (OdmHarvester,),
                {"scraper": odm_reader})


baden_wuerttemberg = def_harvester(BwReader())
# braunschweig       = def_harvester(BraunschweigReader())
# bochum             = def_harvester(BochumReader())
# diepholz           = def_harvester(DiepholzReader())
# koeln              = def_harvester(KoelnReader())
# moers              = def_harvester(MoersReader())
# bremen             = def_harvester(BremenReader())
# rostock            = def_harvester(RostockReader())
