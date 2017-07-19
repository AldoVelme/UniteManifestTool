#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Intel Unite Manifest Tool
#
#  Copyright 2017 AVELAZCX <aldo.alfonsox.velasco.meza@intel.com>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.

from variables import *

class ManifestTool(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        os.path.exists(principal)
        os.path.exists(bsonFolder)
        os.path.exists(binfolder)
        os.path.exists(corebinfolder)
 
        if principal and bsonFolder == True:
            pass
        else:
            os.mkdir(principal)
            os.mkdir(bsonFolder)
    
        if binfolder and corebinfolder == True:
            pass
        else:
            os.mkdir(binfolder)
            os.mkdir(corebinfolder)
            
            
################### DEFINE GENERAL TEST xCASE ###################################
    def test_TC11723(self):
        time.sleep(5)
        #_Manifest_Helper_Tool_Help_start_screen_help
        cmd = subprocess.Popen(exepath, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        cmd.communicate() 
        TC11723 = os.system(echo)
        self.assertEqual(TC11723, 0, errorlevel + '" '  + str(TC11723) + ' "')

    def test_TC11724(self):
        time.sleep(5)
        #_Manifest_Helper_Tool_Help_start_screen_help
        cmd = subprocess.Popen(TC11724, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        cmd.communicate() 
        errcode24 = os.system(echo)
        self.assertEqual(errcode24, 0, errorlevel + '" '  + str(errcode24) + ' "')

    def test_TC11725(self):
        time.sleep(5)
        #_Manifest Helper Tool_Help_error_command
        cmd = subprocess.Popen(TC11725, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        cmd.communicate()
        errcode25 = os.system(echo)
        self.assertEqual(errcode25, 0, errorlevel + '" '  + str(errcode25) + ' "')

    def test_TC11726(self):
        time.sleep(5)
        #_Intel Unite Manifest Tool_Add another dll file and generate a module (plugin) manifest file
        cmd = subprocess.Popen( TC11726, shell=False , stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT )
        cmd.communicate()
        try:
            assert(os.path.isfile(plugbson) == True)
            assert(filecmp.cmp(plugbson, orig_pbson,  shallow=True ) == True)
        except:
            print  errorbson
            raise AssertionError 

    def test_TC11727(self):
        time.sleep(5)
        #_Intel Unite Manifest Tool Core manifest file from binaries
        cmd = subprocess.Popen( TC11727, shell=False , stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT )
        cmd.communicate()
        try:
            assert(os.path.isfile(corebson) == True)
            assert(filecmp.cmp(corebson, orig_cbson,  shallow=True ) == True)
        except:
            print  errorbson
            raise AssertionError

    def test_TC11728(self):
        time.sleep(5)
        #Intel Unite Manifest Tool_Module (plugin) manifest file from binaries
        cmd = subprocess.Popen( TC11728, shell=False , stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT )
        cmd.communicate()
        try:
            assert(os.path.isfile(plugbson) == True)
            assert(filecmp.cmp(plugbson, orig_pbson,  shallow=True ) == True)
        except:
            print  errorcbson
            raise AssertionError

    def test_TC11729(self):
        time.sleep(5)
        #Intel Unite Manifest Tool_Module (plugin) manifest file from   binaries
        cmd = subprocess.Popen( TC11729, shell=False , stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT )
        cmd.communicate()
        self.assertTrue(os.path.isdir(corebinfolder), "ERROR COMPARISON FOLDER")    

        
######################### ERASE TEST FOLDERS #######################################    
    @classmethod
    def tearDownClass(self):
        #It removes folders and files created during the execution of tests.
        print erase
        time.sleep(5)
        shutil.rmtree(rm)
