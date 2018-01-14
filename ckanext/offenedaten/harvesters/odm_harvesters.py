# -*- coding: utf-8 -*-
from ckanext.offenedaten.harvesters.odm_harvester import OdmHarvester
from odm.catalogs.portals.baden_wuerttemberg import BwReader
from odm.catalogs.portals.bayern import BayernReader
from odm.catalogs.portals.braunschweig import BraunschweigReader
from odm.catalogs.portals.bochum import BochumReader
from odm.catalogs.portals.diepholz import DiepholzReader
from odm.catalogs.portals.bremen import BremenReader
from odm.catalogs.portals.rheinland_pfalz import RlpReader
from odm.catalogs.portals.ulm import UlmReader
from odm.catalogs.portals.ckanApiV3 import CkanReader
from odm.catalogs.portals.arnsberg import ArnsbergReader


# Weired way of constructing a python class
def def_harvester(odm_reader):
    return type(odm_reader.info()['name'],
                (OdmHarvester,),
                {"scraper": odm_reader})

arnsberg           = def_harvester(ArnsbergReader())
baden_wuerttemberg = def_harvester(BwReader())
bayern             = def_harvester(BayernReader())
bochum             = def_harvester(BochumReader())
braunschweig       = def_harvester(BraunschweigReader())
bremen             = def_harvester(BremenReader())
diepholz           = def_harvester(DiepholzReader())
moers              = def_harvester(CkanReader('moers'))
krefeld            = def_harvester(CkanReader('krefeld'))
stadtbottrop      = def_harvester(CkanReader('stadt-bottrop')) 
stadtgeldern      = def_harvester(CkanReader('stadt-geldern'))
stadtkleve        = def_harvester(CkanReader('stadt-kleve'))
stadtwesel        = def_harvester(CkanReader('stadt-wesel'))
kreiswesel        = def_harvester(CkanReader('kreis-wesel'))
kreisviersen      = def_harvester(CkanReader('kreis-viersen')) 
kreiskleve        = def_harvester(CkanReader('kreis-kleve'))
gemeindewachtendonk = def_harvester(CkanReader('gemeinde-wachtendonk'))
rheinland_pfalz    = def_harvester(RlpReader())
rostock            = def_harvester(CkanReader('rostock'))
ulm                = def_harvester(UlmReader())
koeln              = def_harvester(CkanReader('koeln'))
bonn               = def_harvester(CkanReader('bonn'))
hamburg            = def_harvester(CkanReader('hamburg'))
frankfurt          = def_harvester(CkanReader('frankfurt'))
aachen             = def_harvester(CkanReader('aachen'))
berlin             = def_harvester(CkanReader('berlin'))
muenchen           = def_harvester(CkanReader('muenchen'))
meerbusch          = def_harvester(CkanReader('meerbusch'))
gelsenkirchen      = def_harvester(CkanReader('gelsenkirchen'))
duesseldorf        = def_harvester(CkanReader('duesseldorf'))
wuppertal          = def_harvester(CkanReader('wuppertal'))
muelheim_ruhr      = def_harvester(CkanReader('muelheim-ruhr'))
leipzig            = def_harvester(CkanReader('leipzig'))
kerpen             = def_harvester(CkanReader('kerpen'))
bergheim           = def_harvester(CkanReader('bergheim'))
bruehl             = def_harvester(CkanReader('brühl'))
kall               = def_harvester(CkanReader('kall'))
elsdorf            = def_harvester(CkanReader('elsdorf'))
euskirchen         = def_harvester(CkanReader('kreis-euskirchen'))
merzenich          = def_harvester(CkanReader('merzenich'))
juelich            = def_harvester(CkanReader('jülich'))
huertgenwald       = def_harvester(CkanReader('hürtgenwald'))
langerwehe         = def_harvester(CkanReader('langerwehe'))
wesseling          = def_harvester(CkanReader('wesseling'))
vettweiss          = def_harvester(CkanReader('vettweiß'))
heimbach           = def_harvester(CkanReader('heimbach'))
kreuzau            = def_harvester(CkanReader('kreuzau'))
linnich            = def_harvester(CkanReader('linnich'))
bad_muenstereifel  = def_harvester(CkanReader('bad-münstereifel'))
titz               = def_harvester(CkanReader('titz'))
bedburg            = def_harvester(CkanReader('bedburg'))
noervenich         = def_harvester(CkanReader('nörvenich'))
niederzier         = def_harvester(CkanReader('niederzier'))
