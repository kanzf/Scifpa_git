# -*- coding: utf-8 -*-

import empro.toolkit.adv as adv

def main():
	path=r"C:/Users/kzf/Desktop/14级-李阳华-研究资料/GF_wrk"
	lib=r"GF_lib"
	subst=r"GF_lib/substrate1.subst"
	substlib=r"GF_lib"
	substname=r"substrate1"
	cell=r"SCFIFMs_Sche"
	view=r"layout"
	libS3D=r"simulation/%G%F_lib/%S%C%F%I%F%Ms_%Sche/_3%D%Viewer/proj_libS3D.xml"
	varDictionary={}
	exprDictionary={}
	hpeesof_dir=r"C:\Program Files\Keysight\ADS2016_01"

	adv.loadDesign(path=path, lib=lib, subst=subst, substlib=substlib, substname=substname, cell=cell, view=view, libS3D=libS3D, var_dict=varDictionary, expr_dict=exprDictionary, hpeesof_dir=hpeesof_dir)
