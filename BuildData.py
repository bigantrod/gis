#Create Joins
arcpy.analysis.SpatialJoin("AddressPoints_20200103", r"HighZones\HighZones", r"C:\Users\anthony.rodriguez\Documents\ArcGIS\Projects\MyProject\MyProject.gdb\AddressPoints_20200103_SpatiHS", "JOIN_ONE_TO_ONE", "KEEP_ALL", r'OBJECTID "OBJECTID" true true false 10 Long 0 10,First,#,AddressPoints_20200103,OBJECTID,-1,-1;ESiteID "ESiteID" true true false 10 Long 0 10,First,#,AddressPoints_20200103,ESiteID,-1,-1;MCode "MCode" true true false 10 Long 0 10,First,#,AddressPoints_20200103,MCode,-1,-1;SiteType "SiteType" true true false 2 Text 0 0,First,#,AddressPoints_20200103,SiteType,0,2;LR "LR" true true false 1 Text 0 0,First,#,AddressPoints_20200103,LR,0,1;Post_Code "Post_Code" true true false 5 Text 0 0,First,#,AddressPoints_20200103,Post_Code,0,5;ESN "ESN" true true false 10 Long 0 10,First,#,AddressPoints_20200103,ESN,-1,-1;Long "Long" true true false 19 Double 0 0,First,#,AddressPoints_20200103,Long,-1,-1;Lat "Lat" true true false 19 Double 0 0,First,#,AddressPoints_20200103,Lat,-1,-1;ParcelNum "ParcelNum" true true false 20 Text 0 0,First,#,AddressPoints_20200103,ParcelNum,0,20;PD "PD" true true false 5 Text 0 0,First,#,AddressPoints_20200103,PD,0,5;PT "PT" true true false 5 Text 0 0,First,#,AddressPoints_20200103,PT,0,5;St_Name "St_Name" true true false 50 Text 0 0,First,#,AddressPoints_20200103,St_Name,0,50;St_PosTyp "St_PosTyp" true true false 5 Text 0 0,First,#,AddressPoints_20200103,St_PosTyp,0,5;St_PosDir "St_PosDir" true true false 5 Text 0 0,First,#,AddressPoints_20200103,St_PosDir,0,5;GeoNameID "GeoNameID" true true false 10 Long 0 10,First,#,AddressPoints_20200103,GeoNameID,-1,-1;ZN "ZN" true true false 50 Text 0 0,First,#,AddressPoints_20200103,ZN,0,50;Add_Number "Add_Number" true true false 15 Text 0 0,First,#,AddressPoints_20200103,Add_Number,0,15;HouseInt "HouseInt" true true false 10 Long 0 10,First,#,AddressPoints_20200103,HouseInt,-1,-1;PrimaryAdd "PrimaryAdd" true true false 100 Text 0 0,First,#,AddressPoints_20200103,PrimaryAdd,0,100;ALIAddress "ALIAddress" true true false 100 Text 0 0,First,#,AddressPoints_20200103,ALIAddress,0,100;AddrLocati "AddrLocati" true true false 2 Text 0 0,First,#,AddressPoints_20200103,AddrLocati,0,2;PrimaryNam "PrimaryNam" true true false 100 Text 0 0,First,#,AddressPoints_20200103,PrimaryNam,0,100;ALIName "ALIName" true true false 100 Text 0 0,First,#,AddressPoints_20200103,ALIName,0,100;Alias1 "Alias1" true true false 60 Text 0 0,First,#,AddressPoints_20200103,Alias1,0,60;Alias2 "Alias2" true true false 60 Text 0 0,First,#,AddressPoints_20200103,Alias2,0,60;Alias3 "Alias3" true true false 60 Text 0 0,First,#,AddressPoints_20200103,Alias3,0,60;Alias4 "Alias4" true true false 60 Text 0 0,First,#,AddressPoints_20200103,Alias4,0,60;Alias5 "Alias5" true true false 60 Text 0 0,First,#,AddressPoints_20200103,Alias5,0,60;DateUpdate "DateUpdate" true true false 19 Double 0 0,First,#,AddressPoints_20200103,DateUpdate,-1,-1;Unit "Unit" true true false 40 Text 0 0,First,#,AddressPoints_20200103,Unit,0,40;County "County" true true false 154 Text 0 0,First,#,AddressPoints_20200103,County,0,154;MailingCit "MailingCit" true true false 254 Text 0 0,First,#,AddressPoints_20200103,MailingCit,0,254;T_MailingC "T_MailingC" true true false 254 Text 0 0,First,#,AddressPoints_20200103,T_MailingC,0,254;Country "Country" true true false 2 Text 0 0,First,#,AddressPoints_20200103,Country,0,2;State "State" true true false 2 Text 0 0,First,#,AddressPoints_20200103,State,0,2;Inc_Muni "Inc_Muni" true true false 50 Text 0 0,First,#,AddressPoints_20200103,Inc_Muni,0,50;OBJECTID_1 "OBJECTID" true true false 0 Long 0 0,First,#,HighZones\HighZones,OBJECTID,-1,-1;SchoolNumb "SchoolNumb" true true false 4 Text 0 0,First,#,HighZones\HighZones,SchoolNumb,0,4;Shape_Leng "Shape_Leng" true true false 0 Double 0 0,First,#,HighZones\HighZones,Shape_Leng,-1,-1;Shape_Le_1 "Shape_Le_1" true true false 0 Double 0 0,First,#,HighZones\HighZones,Shape_Le_1,-1,-1;Shape_STAr "Shape_STAr" true true false 0 Double 0 0,First,#,HighZones\HighZones,Shape_STAr,-1,-1;Shape_STLe "Shape_STLe" true true false 0 Double 0 0,First,#,HighZones\HighZones,Shape_STLe,-1,-1;SchoolName "SchoolName" true true false 50 Text 0 0,First,#,HighZones\HighZones,SchoolName,0,50;created_us "created_us" true true false 254 Text 0 0,First,#,HighZones\HighZones,created_us,0,254;created_da "created_da" true true false 8 Date 0 0,First,#,HighZones\HighZones,created_da,-1,-1;last_edite "last_edite" true true false 254 Text 0 0,First,#,HighZones\HighZones,last_edite,0,254;last_edi_1 "last_edi_1" true true false 8 Date 0 0,First,#,HighZones\HighZones,last_edi_1,-1,-1;Shape_area "Shape_area" true true false 0 Double 0 0,First,#,HighZones\HighZones,Shape_area,-1,-1;Shape_len "Shape_len" true true false 0 Double 0 0,First,#,HighZones\HighZones,Shape_len,-1,-1;Shape__Area "Shape__Area" false true false 0 Double 0 0,First,#,HighZones\HighZones,Shape__Area,-1,-1;Shape__Length "Shape__Length" false true false 0 Double 0 0,First,#,HighZones\HighZones,Shape__Length,-1,-1', "CLOSEST", "1 Miles", '')
arcpy.analysis.SpatialJoin("AddressPoints_20200103", "NewMiddleZone", r"C:\Users\anthony.rodriguez\Documents\ArcGIS\Projects\MyProject\MyProject.gdb\AddressPoints_20200103_SpatiMS", "JOIN_ONE_TO_ONE", "KEEP_ALL", 'OBJECTID "OBJECTID" true true false 10 Long 0 10,First,#,AddressPoints_20200103,OBJECTID,-1,-1;ESiteID "ESiteID" true true false 10 Long 0 10,First,#,AddressPoints_20200103,ESiteID,-1,-1;MCode "MCode" true true false 10 Long 0 10,First,#,AddressPoints_20200103,MCode,-1,-1;SiteType "SiteType" true true false 2 Text 0 0,First,#,AddressPoints_20200103,SiteType,0,2;LR "LR" true true false 1 Text 0 0,First,#,AddressPoints_20200103,LR,0,1;Post_Code "Post_Code" true true false 5 Text 0 0,First,#,AddressPoints_20200103,Post_Code,0,5;ESN "ESN" true true false 10 Long 0 10,First,#,AddressPoints_20200103,ESN,-1,-1;Long "Long" true true false 19 Double 0 0,First,#,AddressPoints_20200103,Long,-1,-1;Lat "Lat" true true false 19 Double 0 0,First,#,AddressPoints_20200103,Lat,-1,-1;ParcelNum "ParcelNum" true true false 20 Text 0 0,First,#,AddressPoints_20200103,ParcelNum,0,20;PD "PD" true true false 5 Text 0 0,First,#,AddressPoints_20200103,PD,0,5;PT "PT" true true false 5 Text 0 0,First,#,AddressPoints_20200103,PT,0,5;St_Name "St_Name" true true false 50 Text 0 0,First,#,AddressPoints_20200103,St_Name,0,50;St_PosTyp "St_PosTyp" true true false 5 Text 0 0,First,#,AddressPoints_20200103,St_PosTyp,0,5;St_PosDir "St_PosDir" true true false 5 Text 0 0,First,#,AddressPoints_20200103,St_PosDir,0,5;GeoNameID "GeoNameID" true true false 10 Long 0 10,First,#,AddressPoints_20200103,GeoNameID,-1,-1;ZN "ZN" true true false 50 Text 0 0,First,#,AddressPoints_20200103,ZN,0,50;Add_Number "Add_Number" true true false 15 Text 0 0,First,#,AddressPoints_20200103,Add_Number,0,15;HouseInt "HouseInt" true true false 10 Long 0 10,First,#,AddressPoints_20200103,HouseInt,-1,-1;PrimaryAdd "PrimaryAdd" true true false 100 Text 0 0,First,#,AddressPoints_20200103,PrimaryAdd,0,100;ALIAddress "ALIAddress" true true false 100 Text 0 0,First,#,AddressPoints_20200103,ALIAddress,0,100;AddrLocati "AddrLocati" true true false 2 Text 0 0,First,#,AddressPoints_20200103,AddrLocati,0,2;PrimaryNam "PrimaryNam" true true false 100 Text 0 0,First,#,AddressPoints_20200103,PrimaryNam,0,100;ALIName "ALIName" true true false 100 Text 0 0,First,#,AddressPoints_20200103,ALIName,0,100;Alias1 "Alias1" true true false 60 Text 0 0,First,#,AddressPoints_20200103,Alias1,0,60;Alias2 "Alias2" true true false 60 Text 0 0,First,#,AddressPoints_20200103,Alias2,0,60;Alias3 "Alias3" true true false 60 Text 0 0,First,#,AddressPoints_20200103,Alias3,0,60;Alias4 "Alias4" true true false 60 Text 0 0,First,#,AddressPoints_20200103,Alias4,0,60;Alias5 "Alias5" true true false 60 Text 0 0,First,#,AddressPoints_20200103,Alias5,0,60;DateUpdate "DateUpdate" true true false 19 Double 0 0,First,#,AddressPoints_20200103,DateUpdate,-1,-1;Unit "Unit" true true false 40 Text 0 0,First,#,AddressPoints_20200103,Unit,0,40;County "County" true true false 154 Text 0 0,First,#,AddressPoints_20200103,County,0,154;MailingCit "MailingCit" true true false 254 Text 0 0,First,#,AddressPoints_20200103,MailingCit,0,254;T_MailingC "T_MailingC" true true false 254 Text 0 0,First,#,AddressPoints_20200103,T_MailingC,0,254;Country "Country" true true false 2 Text 0 0,First,#,AddressPoints_20200103,Country,0,2;State "State" true true false 2 Text 0 0,First,#,AddressPoints_20200103,State,0,2;Inc_Muni "Inc_Muni" true true false 50 Text 0 0,First,#,AddressPoints_20200103,Inc_Muni,0,50;SchoolNumb "SchoolNumb" true true false 4 Text 0 0,First,#,NewMiddleZone,SchoolNumb,0,4;Shape_Leng "Shape_Leng" true true false 8 Double 0 0,First,#,NewMiddleZone,Shape_Leng,-1,-1;Shape_STAr "Shape_STAr" true true false 8 Double 0 0,First,#,NewMiddleZone,Shape_STAr,-1,-1;Shape_STLe "Shape_STLe" true true false 8 Double 0 0,First,#,NewMiddleZone,Shape_STLe,-1,-1;SchoolName "SchoolName" true true false 50 Text 0 0,First,#,NewMiddleZone,SchoolName,0,50;created_us "created_us" true true false 254 Text 0 0,First,#,NewMiddleZone,created_us,0,254;created_da "created_da" true true false 8 Date 0 0,First,#,NewMiddleZone,created_da,-1,-1;last_edite "last_edite" true true false 254 Text 0 0,First,#,NewMiddleZone,last_edite,0,254;last_edi_1 "last_edi_1" true true false 8 Date 0 0,First,#,NewMiddleZone,last_edi_1,-1,-1;Shape_ST_1 "Shape_ST_1" true true false 8 Double 0 0,First,#,NewMiddleZone,Shape_ST_1,-1,-1;Shape_ST_2 "Shape_ST_2" true true false 8 Double 0 0,First,#,NewMiddleZone,Shape_ST_2,-1,-1;Shape__Area "Shape__Area" true true false 8 Double 0 0,First,#,NewMiddleZone,Shape__Area,-1,-1;Shape__Length "Shape__Length" true true false 8 Double 0 0,First,#,NewMiddleZone,Shape__Length,-1,-1;Shape_Length "Shape_Length" false true true 8 Double 0 0,First,#,NewMiddleZone,Shape_Length,-1,-1;Shape_Area "Shape_Area" false true true 8 Double 0 0,First,#,NewMiddleZone,Shape_Area,-1,-1', "CLOSEST", "1 Miles", '')
arcpy.analysis.SpatialJoin("AddressPoints_20200103", r"ElementaryZones\ElementaryZones", r"C:\Users\anthony.rodriguez\Documents\ArcGIS\Projects\MyProject\MyProject.gdb\AddressPoints_20200103_SpatiEL", "JOIN_ONE_TO_ONE", "KEEP_ALL", r'OBJECTID "OBJECTID" true true false 10 Long 0 10,First,#,AddressPoints_20200103,OBJECTID,-1,-1;ESiteID "ESiteID" true true false 10 Long 0 10,First,#,AddressPoints_20200103,ESiteID,-1,-1;MCode "MCode" true true false 10 Long 0 10,First,#,AddressPoints_20200103,MCode,-1,-1;SiteType "SiteType" true true false 2 Text 0 0,First,#,AddressPoints_20200103,SiteType,0,2;LR "LR" true true false 1 Text 0 0,First,#,AddressPoints_20200103,LR,0,1;Post_Code "Post_Code" true true false 5 Text 0 0,First,#,AddressPoints_20200103,Post_Code,0,5;ESN "ESN" true true false 10 Long 0 10,First,#,AddressPoints_20200103,ESN,-1,-1;Long "Long" true true false 19 Double 0 0,First,#,AddressPoints_20200103,Long,-1,-1;Lat "Lat" true true false 19 Double 0 0,First,#,AddressPoints_20200103,Lat,-1,-1;ParcelNum "ParcelNum" true true false 20 Text 0 0,First,#,AddressPoints_20200103,ParcelNum,0,20;PD "PD" true true false 5 Text 0 0,First,#,AddressPoints_20200103,PD,0,5;PT "PT" true true false 5 Text 0 0,First,#,AddressPoints_20200103,PT,0,5;St_Name "St_Name" true true false 50 Text 0 0,First,#,AddressPoints_20200103,St_Name,0,50;St_PosTyp "St_PosTyp" true true false 5 Text 0 0,First,#,AddressPoints_20200103,St_PosTyp,0,5;St_PosDir "St_PosDir" true true false 5 Text 0 0,First,#,AddressPoints_20200103,St_PosDir,0,5;GeoNameID "GeoNameID" true true false 10 Long 0 10,First,#,AddressPoints_20200103,GeoNameID,-1,-1;ZN "ZN" true true false 50 Text 0 0,First,#,AddressPoints_20200103,ZN,0,50;Add_Number "Add_Number" true true false 15 Text 0 0,First,#,AddressPoints_20200103,Add_Number,0,15;HouseInt "HouseInt" true true false 10 Long 0 10,First,#,AddressPoints_20200103,HouseInt,-1,-1;PrimaryAdd "PrimaryAdd" true true false 100 Text 0 0,First,#,AddressPoints_20200103,PrimaryAdd,0,100;ALIAddress "ALIAddress" true true false 100 Text 0 0,First,#,AddressPoints_20200103,ALIAddress,0,100;AddrLocati "AddrLocati" true true false 2 Text 0 0,First,#,AddressPoints_20200103,AddrLocati,0,2;PrimaryNam "PrimaryNam" true true false 100 Text 0 0,First,#,AddressPoints_20200103,PrimaryNam,0,100;ALIName "ALIName" true true false 100 Text 0 0,First,#,AddressPoints_20200103,ALIName,0,100;Alias1 "Alias1" true true false 60 Text 0 0,First,#,AddressPoints_20200103,Alias1,0,60;Alias2 "Alias2" true true false 60 Text 0 0,First,#,AddressPoints_20200103,Alias2,0,60;Alias3 "Alias3" true true false 60 Text 0 0,First,#,AddressPoints_20200103,Alias3,0,60;Alias4 "Alias4" true true false 60 Text 0 0,First,#,AddressPoints_20200103,Alias4,0,60;Alias5 "Alias5" true true false 60 Text 0 0,First,#,AddressPoints_20200103,Alias5,0,60;DateUpdate "DateUpdate" true true false 19 Double 0 0,First,#,AddressPoints_20200103,DateUpdate,-1,-1;Unit "Unit" true true false 40 Text 0 0,First,#,AddressPoints_20200103,Unit,0,40;County "County" true true false 154 Text 0 0,First,#,AddressPoints_20200103,County,0,154;MailingCit "MailingCit" true true false 254 Text 0 0,First,#,AddressPoints_20200103,MailingCit,0,254;T_MailingC "T_MailingC" true true false 254 Text 0 0,First,#,AddressPoints_20200103,T_MailingC,0,254;Country "Country" true true false 2 Text 0 0,First,#,AddressPoints_20200103,Country,0,2;State "State" true true false 2 Text 0 0,First,#,AddressPoints_20200103,State,0,2;Inc_Muni "Inc_Muni" true true false 50 Text 0 0,First,#,AddressPoints_20200103,Inc_Muni,0,50;SchoolName "SchoolName" true true false 30 Text 0 0,First,#,ElementaryZones\ElementaryZones,SchoolName,0,30;SchoolNumb "SchoolNumb" true true false 4 Text 0 0,First,#,ElementaryZones\ElementaryZones,SchoolNumb,0,4;Shape_STAr "Shape_STAr" true true false 0 Double 0 0,First,#,ElementaryZones\ElementaryZones,Shape_STAr,-1,-1;Shape_STLe "Shape_STLe" true true false 0 Double 0 0,First,#,ElementaryZones\ElementaryZones,Shape_STLe,-1,-1;Shape_ST_1 "Shape_ST_1" true true false 0 Double 0 0,First,#,ElementaryZones\ElementaryZones,Shape_ST_1,-1,-1;Shape_ST_2 "Shape_ST_2" true true false 0 Double 0 0,First,#,ElementaryZones\ElementaryZones,Shape_ST_2,-1,-1;created_us "created_us" true true false 254 Text 0 0,First,#,ElementaryZones\ElementaryZones,created_us,0,254;created_da "created_da" true true false 8 Date 0 0,First,#,ElementaryZones\ElementaryZones,created_da,-1,-1;last_edite "last_edite" true true false 254 Text 0 0,First,#,ElementaryZones\ElementaryZones,last_edite,0,254;last_edi_1 "last_edi_1" true true false 8 Date 0 0,First,#,ElementaryZones\ElementaryZones,last_edi_1,-1,-1;Shape_ST_3 "Shape_ST_3" true true false 0 Double 0 0,First,#,ElementaryZones\ElementaryZones,Shape_ST_3,-1,-1;Shape_ST_4 "Shape_ST_4" true true false 0 Double 0 0,First,#,ElementaryZones\ElementaryZones,Shape_ST_4,-1,-1;Shape__Area "Shape__Area" false true false 0 Double 0 0,First,#,ElementaryZones\ElementaryZones,Shape__Area,-1,-1;Shape__Length "Shape__Length" false true false 0 Double 0 0,First,#,ElementaryZones\ElementaryZones,Shape__Length,-1,-1', "CLOSEST", "1 Miles", '')
arcpy.analysis.SpatialJoin("AddressPoints_20200103", r"MagnetZones\MagnetZones", r"C:\Users\anthony.rodriguez\Documents\ArcGIS\Projects\MyProject\MyProject.gdb\AddressPoints_20200103_SpatiMAG", "JOIN_ONE_TO_ONE", "KEEP_ALL", r'OBJECTID "OBJECTID" true true false 10 Long 0 10,First,#,AddressPoints_20200103,OBJECTID,-1,-1;ESiteID "ESiteID" true true false 10 Long 0 10,First,#,AddressPoints_20200103,ESiteID,-1,-1;MCode "MCode" true true false 10 Long 0 10,First,#,AddressPoints_20200103,MCode,-1,-1;SiteType "SiteType" true true false 2 Text 0 0,First,#,AddressPoints_20200103,SiteType,0,2;LR "LR" true true false 1 Text 0 0,First,#,AddressPoints_20200103,LR,0,1;Post_Code "Post_Code" true true false 5 Text 0 0,First,#,AddressPoints_20200103,Post_Code,0,5;ESN "ESN" true true false 10 Long 0 10,First,#,AddressPoints_20200103,ESN,-1,-1;Long "Long" true true false 19 Double 0 0,First,#,AddressPoints_20200103,Long,-1,-1;Lat "Lat" true true false 19 Double 0 0,First,#,AddressPoints_20200103,Lat,-1,-1;ParcelNum "ParcelNum" true true false 20 Text 0 0,First,#,AddressPoints_20200103,ParcelNum,0,20;PD "PD" true true false 5 Text 0 0,First,#,AddressPoints_20200103,PD,0,5;PT "PT" true true false 5 Text 0 0,First,#,AddressPoints_20200103,PT,0,5;St_Name "St_Name" true true false 50 Text 0 0,First,#,AddressPoints_20200103,St_Name,0,50;St_PosTyp "St_PosTyp" true true false 5 Text 0 0,First,#,AddressPoints_20200103,St_PosTyp,0,5;St_PosDir "St_PosDir" true true false 5 Text 0 0,First,#,AddressPoints_20200103,St_PosDir,0,5;GeoNameID "GeoNameID" true true false 10 Long 0 10,First,#,AddressPoints_20200103,GeoNameID,-1,-1;ZN "ZN" true true false 50 Text 0 0,First,#,AddressPoints_20200103,ZN,0,50;Add_Number "Add_Number" true true false 15 Text 0 0,First,#,AddressPoints_20200103,Add_Number,0,15;HouseInt "HouseInt" true true false 10 Long 0 10,First,#,AddressPoints_20200103,HouseInt,-1,-1;PrimaryAdd "PrimaryAdd" true true false 100 Text 0 0,First,#,AddressPoints_20200103,PrimaryAdd,0,100;ALIAddress "ALIAddress" true true false 100 Text 0 0,First,#,AddressPoints_20200103,ALIAddress,0,100;AddrLocati "AddrLocati" true true false 2 Text 0 0,First,#,AddressPoints_20200103,AddrLocati,0,2;PrimaryNam "PrimaryNam" true true false 100 Text 0 0,First,#,AddressPoints_20200103,PrimaryNam,0,100;ALIName "ALIName" true true false 100 Text 0 0,First,#,AddressPoints_20200103,ALIName,0,100;Alias1 "Alias1" true true false 60 Text 0 0,First,#,AddressPoints_20200103,Alias1,0,60;Alias2 "Alias2" true true false 60 Text 0 0,First,#,AddressPoints_20200103,Alias2,0,60;Alias3 "Alias3" true true false 60 Text 0 0,First,#,AddressPoints_20200103,Alias3,0,60;Alias4 "Alias4" true true false 60 Text 0 0,First,#,AddressPoints_20200103,Alias4,0,60;Alias5 "Alias5" true true false 60 Text 0 0,First,#,AddressPoints_20200103,Alias5,0,60;DateUpdate "DateUpdate" true true false 19 Double 0 0,First,#,AddressPoints_20200103,DateUpdate,-1,-1;Unit "Unit" true true false 40 Text 0 0,First,#,AddressPoints_20200103,Unit,0,40;County "County" true true false 154 Text 0 0,First,#,AddressPoints_20200103,County,0,154;MailingCit "MailingCit" true true false 254 Text 0 0,First,#,AddressPoints_20200103,MailingCit,0,254;T_MailingC "T_MailingC" true true false 254 Text 0 0,First,#,AddressPoints_20200103,T_MailingC,0,254;Country "Country" true true false 2 Text 0 0,First,#,AddressPoints_20200103,Country,0,2;State "State" true true false 2 Text 0 0,First,#,AddressPoints_20200103,State,0,2;Inc_Muni "Inc_Muni" true true false 50 Text 0 0,First,#,AddressPoints_20200103,Inc_Muni,0,50;OBJECTID_1 "OBJECTID" true true false 0 Long 0 0,First,#,MagnetZones\MagnetZones,OBJECTID,-1,-1;SchoolName "SchoolName" true true false 50 Text 0 0,First,#,MagnetZones\MagnetZones,SchoolName,0,50;SchoolNumb "SchoolNumb" true true false 4 Text 0 0,First,#,MagnetZones\MagnetZones,SchoolNumb,0,4;Shape_Leng "Shape_Leng" true true false 0 Double 0 0,First,#,MagnetZones\MagnetZones,Shape_Leng,-1,-1;Shape_STAr "Shape_STAr" true true false 0 Double 0 0,First,#,MagnetZones\MagnetZones,Shape_STAr,-1,-1;Shape_STLe "Shape_STLe" true true false 0 Double 0 0,First,#,MagnetZones\MagnetZones,Shape_STLe,-1,-1;Shape_area "Shape_area" true true false 0 Double 0 0,First,#,MagnetZones\MagnetZones,Shape_area,-1,-1;Shape_len "Shape_len" true true false 0 Double 0 0,First,#,MagnetZones\MagnetZones,Shape_len,-1,-1;Shape__Area "Shape__Area" false true false 0 Double 0 0,First,#,MagnetZones\MagnetZones,Shape__Area,-1,-1;Shape__Length "Shape__Length" false true false 0 Double 0 0,First,#,MagnetZones\MagnetZones,Shape__Length,-1,-1', "CLOSEST", "1 Miles", '')
arcpy.analysis.SpatialJoin("AddressPoints_20200103", r"IBZones\IBZones", r"C:\Users\anthony.rodriguez\Documents\ArcGIS\Projects\MyProject\MyProject.gdb\AddressPoints_20200103_SpatiIB", "JOIN_ONE_TO_ONE", "KEEP_ALL", r'OBJECTID "OBJECTID" true true false 10 Long 0 10,First,#,AddressPoints_20200103,OBJECTID,-1,-1;ESiteID "ESiteID" true true false 10 Long 0 10,First,#,AddressPoints_20200103,ESiteID,-1,-1;MCode "MCode" true true false 10 Long 0 10,First,#,AddressPoints_20200103,MCode,-1,-1;SiteType "SiteType" true true false 2 Text 0 0,First,#,AddressPoints_20200103,SiteType,0,2;LR "LR" true true false 1 Text 0 0,First,#,AddressPoints_20200103,LR,0,1;Post_Code "Post_Code" true true false 5 Text 0 0,First,#,AddressPoints_20200103,Post_Code,0,5;ESN "ESN" true true false 10 Long 0 10,First,#,AddressPoints_20200103,ESN,-1,-1;Long "Long" true true false 19 Double 0 0,First,#,AddressPoints_20200103,Long,-1,-1;Lat "Lat" true true false 19 Double 0 0,First,#,AddressPoints_20200103,Lat,-1,-1;ParcelNum "ParcelNum" true true false 20 Text 0 0,First,#,AddressPoints_20200103,ParcelNum,0,20;PD "PD" true true false 5 Text 0 0,First,#,AddressPoints_20200103,PD,0,5;PT "PT" true true false 5 Text 0 0,First,#,AddressPoints_20200103,PT,0,5;St_Name "St_Name" true true false 50 Text 0 0,First,#,AddressPoints_20200103,St_Name,0,50;St_PosTyp "St_PosTyp" true true false 5 Text 0 0,First,#,AddressPoints_20200103,St_PosTyp,0,5;St_PosDir "St_PosDir" true true false 5 Text 0 0,First,#,AddressPoints_20200103,St_PosDir,0,5;GeoNameID "GeoNameID" true true false 10 Long 0 10,First,#,AddressPoints_20200103,GeoNameID,-1,-1;ZN "ZN" true true false 50 Text 0 0,First,#,AddressPoints_20200103,ZN,0,50;Add_Number "Add_Number" true true false 15 Text 0 0,First,#,AddressPoints_20200103,Add_Number,0,15;HouseInt "HouseInt" true true false 10 Long 0 10,First,#,AddressPoints_20200103,HouseInt,-1,-1;PrimaryAdd "PrimaryAdd" true true false 100 Text 0 0,First,#,AddressPoints_20200103,PrimaryAdd,0,100;ALIAddress "ALIAddress" true true false 100 Text 0 0,First,#,AddressPoints_20200103,ALIAddress,0,100;AddrLocati "AddrLocati" true true false 2 Text 0 0,First,#,AddressPoints_20200103,AddrLocati,0,2;PrimaryNam "PrimaryNam" true true false 100 Text 0 0,First,#,AddressPoints_20200103,PrimaryNam,0,100;ALIName "ALIName" true true false 100 Text 0 0,First,#,AddressPoints_20200103,ALIName,0,100;Alias1 "Alias1" true true false 60 Text 0 0,First,#,AddressPoints_20200103,Alias1,0,60;Alias2 "Alias2" true true false 60 Text 0 0,First,#,AddressPoints_20200103,Alias2,0,60;Alias3 "Alias3" true true false 60 Text 0 0,First,#,AddressPoints_20200103,Alias3,0,60;Alias4 "Alias4" true true false 60 Text 0 0,First,#,AddressPoints_20200103,Alias4,0,60;Alias5 "Alias5" true true false 60 Text 0 0,First,#,AddressPoints_20200103,Alias5,0,60;DateUpdate "DateUpdate" true true false 19 Double 0 0,First,#,AddressPoints_20200103,DateUpdate,-1,-1;Unit "Unit" true true false 40 Text 0 0,First,#,AddressPoints_20200103,Unit,0,40;County "County" true true false 154 Text 0 0,First,#,AddressPoints_20200103,County,0,154;MailingCit "MailingCit" true true false 254 Text 0 0,First,#,AddressPoints_20200103,MailingCit,0,254;T_MailingC "T_MailingC" true true false 254 Text 0 0,First,#,AddressPoints_20200103,T_MailingC,0,254;Country "Country" true true false 2 Text 0 0,First,#,AddressPoints_20200103,Country,0,2;State "State" true true false 2 Text 0 0,First,#,AddressPoints_20200103,State,0,2;Inc_Muni "Inc_Muni" true true false 50 Text 0 0,First,#,AddressPoints_20200103,Inc_Muni,0,50;OBJECTID_1 "OBJECTID" true true false 0 Long 0 0,First,#,IBZones\IBZones,OBJECTID,-1,-1;SchoolName "SchoolName" true true false 50 Text 0 0,First,#,IBZones\IBZones,SchoolName,0,50;SchoolNumb "SchoolNumb" true true false 4 Text 0 0,First,#,IBZones\IBZones,SchoolNumb,0,4;Shape_area "Shape_area" true true false 0 Double 0 0,First,#,IBZones\IBZones,Shape_area,-1,-1;Shape_len "Shape_len" true true false 0 Double 0 0,First,#,IBZones\IBZones,Shape_len,-1,-1;Shape__Area "Shape__Area" false true false 0 Double 0 0,First,#,IBZones\IBZones,Shape__Area,-1,-1;Shape__Length "Shape__Length" false true false 0 Double 0 0,First,#,IBZones\IBZones,Shape__Length,-1,-1', "CLOSEST", "1 Miles", '')
