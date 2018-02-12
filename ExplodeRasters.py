import arcpy,os,sys,string
from arcpy.sa import *

arcpy.CheckOutExtension("Spatial") #raster processing requires spatial analyst extension



class Toolbox(object):
    def __init__(self):
        self.label =  "Exploding Rasters"
        self.alias  = "ER"

        # List of tool classes associated with this toolbox
        self.tools = [ExplodeRasters]





class ExplodeRasters(object):
    def __init__(self):
        self.label       = "Explode Rasters"
        self.description = " This tool will take an input multiband raster and " +\
                           " extract all or some of its individual bands, saving these " +\
                           " bands as separate single band rasters. Additionally, it will create NDVI and SAVI images." + \
                           " Exploding Rasters is everythying you've ever hoped for and dreamed of." + \
                           "  It's perfection."




    def getParameterInfo(self):

        # Input Features parameter
        in_features = arcpy.Parameter(
            displayName="Input Raster",
            name="in_features",
            datatype="DERasterDataset",
            parameterType="Required",
            direction="Input")

        # create select all bands button
        all_bands = arcpy.Parameter(
            displayName="Select all bands",
            name="Select_All",
            datatype="Boolean",
            parameterType="Required",
            direction="Input")
        all_bands.value="true" #user sees the checkbox already checked off

    #Raster types options
        TIFF = arcpy.Parameter(
            displayName="TIFF",
            name ="TIFF",
            datatype="Boolean",
            parameterType="Optional",
            direction="Input")
        BMP = arcpy.Parameter(
            displayName="BMP",
            name="bmp",
            datatype="Boolean",
            parameterType="Optional",
            direction="Input")
        PNG = arcpy.Parameter(
            displayName="PNG",
            name="png",
            datatype="Boolean",
            parameterType="Optional",
            direction="Input")

        # Range of Desired Bands parameter
        select_bands = arcpy.Parameter(
            displayName="Select Bands",
            name="Select_Bands",
            datatype="String",
            parameterType="Optional",
            direction="Input")


        #select bands for NDVI and SAVI band parameters
        NDVI_red = arcpy.Parameter(
            displayName="Select a red band for NDVI and SAVI calculation",
            name="NDVI_bRed",
            datatype="String",
            parameterType="Optional",
            direction="Input")

        NDVI_NIR = arcpy.Parameter(
            displayName="Select a NIR band for NDVI and SAVI calculation",
            name="NDVI_BNIR",
            datatype="String",
            parameterType="Optional",
            direction="Input")
	NDVI_NIR.enabled= False  #gray out the NIR band parameter until user enters a red band selection

        #out directory
        OutDir = arcpy.Parameter(
            displayName="Output Workspace",
            name="Out_Directory",
            datatype="DEWorkspace",
            parameterType="Required",
            direction="Input")

        # Create filename output prefix
        prefix = arcpy.Parameter(
            displayName="Output filename prefix",
            name="output_prefix",
            datatype="GPString",
            parameterType="Required",
            direction="Input")

        parameters = [in_features, all_bands, select_bands, NDVI_red, NDVI_NIR, prefix, OutDir, TIFF, BMP, PNG]

        return parameters


	#execution code
    def execute(self, parameters, messages):
        #accessing the parameters list and retrieving values as text
        in_raster=parameters[0].valueAsText
        ALL = parameters[1].valueAsText
        Bands = parameters[2].valueAsText
        Red = parameters[3].valueAsText
        NIR = parameters[4].valueAsText
        prefix = parameters[5].valueAsText
        Out_Dir = parameters[6].valueAsText
        TIFF = parameters[7].valueAsText
        BMP = parameters[8].valueAsText
        PNG = parameters[9].valueAsText

        #adding messages for the user 
        messages.addMessage("INPUT RASTER=" +in_raster)
        messages.addMessage("\n" + "Yay, you're doing great!") #necessary encouragement for users

        #specifying the workspace as the input raster and initiating overwrite
        arcpy.env.workspace=in_raster
        arcpy.env.overwriteOutput = True #must overwrite because single bands within multiband raster already exist

	#options for output format type
        if TIFF == "true": #output tif if TIF box is checked
            assignment = ".tif"
            ending = "TIFF"
	    
	    #surprise congratulatory text file for user:)
	    outfile=os.path.join(Out_Dir, "Inspiration.txt")
	    #open file
	    f=open(outfile, "w")
	    f.write("Congratulations on exploding your rasters! Here are some words of encouragement for the rest of your GIS analysis.")
	    f.write("\n" "\n" "You are amazing, and you are smart, and you are beautiful.")
	    f.write("\n" "\n" "I believe in you.")
	    f.write("\n" "\n" "Go light up the world, you glittering ray of sunshine!")
	    f.close()

            messages.addMessage("That was a good output choice.")
        elif BMP == "true": #output bmp if BMP box is checked
            assignment = ".bmp"
            ending = "BMP"

            #surprise congratulatory text file for user:)
	    outfile=os.path.join(Out_Dir, "Inspiration.txt")
	    #open file
	    f=open(outfile, "w")
	    f.write("Congratulations on exploding your rasters! Here are some words of encouragement for the rest of your GIS analysis.")
	    f.write("\n" "\n" "You are amazing, and you are smart, and you are beautiful.")
	    f.write("\n" "\n" "I believe in you.")
	    f.write("\n" "\n" "Go light up the world, you glittering ray of sunshine!")
	    f.close()

        elif PNG == "true": #output png if PNG box is checked
            assignment = ".png"
            ending = "PNG"

	    #surprise congratulatory text file for user:)
	    outfile=os.path.join(Out_Dir, "Inspiration.txt")
	    outfile=os.path.join(Out_Dir, "Inspiration.txt")
	    #open file
	    f=open(outfile, "w")
	    f.write("Congratulations on exploding your rasters! Here are some words of encouragement for the rest of your GIS analysis.")
	    f.write("\n" "\n" "You are amazing, and you are smart, and you are beautiful.")
	    f.write("\n" "\n" "I believe in you.")
	    f.write("\n" "\n" "Go light up the world, you glittering ray of sunshine!")
	    f.close()

	#default to TIFF if user forgets an output format
        else:
            messages.addWarningMessage("You forgot to select an extension. The process will default to using the TIFF output format.")
            assignment = ".tif"
            ending = "TIFF"

	    #surprise congratulatory text file for user:)
	    outfile=os.path.join(Out_Dir, "Inspiration.txt")
	    #open file
	    f=open(outfile, "w")
	    f.write("Congratulations on exploding your rasters! Here are some words of encouragement for the rest of your GIS analysis.")
	    f.write("\n" "\n" "You are amazing, and you are smart, and you are beautiful.")
	    f.write("\n" "\n" "I believe in you.")
	    f.write("\n" "\n" "Go light up the world, you glittering ray of sunshine!")
	    f.close()
	
	#NDVI and SAVI calculations
	if parameters[3].value and parameters[4].value:
	    messages.addMessage("Without rain, there is no growth.")

            bands_in_input = [] #create empty list and append with all possible bands contained in raster
            ListBandNames = arcpy.ListRasters()


            for band in ListBandNames: 
                bndDesc = arcpy.Describe(band)
                bands_in_input.append(band) #append all bands to list
                NoData = bndDesc.noDataValue

            Input_Red=Red.split(",") #splitting comma separated red string user input and creating a list
            Updated_Red =["Band_" + band for band in Input_Red] #adding "Band_" to all elements in Input_Red list so that their names match elements in bands_in_input list 
            Input_NIR=NIR.split(",") #splitting comma separated NIR string user input and creating a list
            Updated_NIR =["Band_" + band for band in Input_NIR] #adding "Band_" to all elements in Input_NIR list so that their names match elements in bands_in_input list 

            Red_result = [] #create empty list for elements common to bands_in_input and Input_Red 
            NIR_result = [] #create empty list for elements common to bands_in_input and Input_NIR

            for element in bands_in_input: #add elements common to bands_in_input and Input_Red  to Red_result
                if element in Updated_Red:
                    Red_result.append(element)
            
            NDVI_red=arcpy.sa.Float(Red_result[0]) #convert to float to be used for NDVI and SAVI calculation

            for element in bands_in_input: #add elements common to bands_in_input and Input_Red  to NIR_result
                if element in Updated_NIR:
                    NIR_result.append(element)
            for nir in NIR_result:
                NDVI_NIR=arcpy.sa.Float(nir)#convert to float to be used for NDVI and SAVI calculation
                
            #NDVI calculations
            NDVI_num=arcpy.sa.Float(NDVI_NIR-NDVI_red)
            NDVI_denom=arcpy.sa.Float(NDVI_NIR+NDVI_red)
            sr=arcpy.sa.Con(NDVI_red<>0, NDVI_num/NDVI_denom, -9999) #avoid diving by 0
            NDVI_calc=arcpy.sa.Divide(NDVI_num,NDVI_denom)
            Out_NDVI= os.path.join (Out_Dir, prefix + "NDVI" + assignment)
            arcpy.CopyRaster_management(NDVI_calc, Out_NDVI, format = ending, nodata_value = NoData)

            #SAVI calculations
            SAVI_num=arcpy.sa.Float(NDVI_NIR-NDVI_red)
            SAVI_denom=arcpy.sa.Float(NDVI_NIR+NDVI_red-0.5)
            SAVI_sr=arcpy.sa.Con(NDVI_red<>0, NDVI_num/NDVI_denom*1.5, -9999) #avoid dividing by 0
            SAVI_calc=SAVI_num/SAVI_denom*1.5
            Out_SAVI= os.path.join (Out_Dir, prefix + "SAVI" + assignment)
            arcpy.CopyRaster_management(SAVI_calc, Out_SAVI, format = ending, nodata_value = NoData)

        #test if the user wants all bands exploded
        if ALL == "true":
            ListBandNames = arcpy.ListRasters() #list all bands in input raster
            for band in ListBandNames: #copy every band
                bndDesc = arcpy.Describe(band)
                NoData = bndDesc.noDataValue
                outRaster = os.path.join(Out_Dir, prefix + band + assignment)
                arcpy.CopyRaster_management(band, outRaster, format = ending, nodata_value = NoData)

         #else if the user has not selected all and instead will only export specific bands
        elif parameters[2].value:
            messages.addMessage("Someone loves you:)")
            bands_in_input = [] #create empty list for all possible bands in input raster
            ListBandNames = arcpy.ListRasters()

            for band in ListBandNames: #append list of all bands to bands_in_input
                bndDesc = arcpy.Describe(band)
                bands_in_input.append(band)
                NoData = bndDesc.noDataValue

            UserInput_Select = Bands.split(",") #split comma separated string of bands of interst and create a list
            UpdatedInput =["Band_" + band for band in UserInput_Select] #adding "Band_" to all elements in UpdatedInput so that their names exactly match elements in bands_in_input list

            result = [] #create new empty list for bands common to UpdatedInput and bands_in_input
            for element in bands_in_input:
                if element in UpdatedInput:
                    result.append(element) #add bands common to UpdatedInput and bands_in_input to result list
                    outRaster = os.path.join(Out_Dir, prefix + element + assignment)
                    arcpy.CopyRaster_management(element, outRaster, format = ending, nodata_value = NoData) #copy bands of interest

        #default
	else:
            messages.addWarningMessage("You forgot to select an extension. The process will default to using the TIFF output format.")

            #copying TIFF rasters
            ListBandNames = arcpy.ListRasters()
            for band in ListBandNames:
                bndDesc = arcpy.Describe(band)
                NoData = bndDesc.noDataValue
                outRaster = os.path.join(Out_Dir, prefix + band + assignment)
                arcpy.CopyRaster_management(band, outRaster, format = ending, nodata_value = NoData)

	    #surprise congratulatory text file
	    outfile=os.path.join(Out_Dir, "Inspiration.txt")
	    #open file
	    f.write("Congratulations on exploding your rasters! Here are some words of encouragement for the rest of your GIS analysis.")
	    f.write("\n" "\n" "You are amazing, and you are smart, and you are beautiful.")
	    f.write("\n" "\n" "I believe in you.")
	    f.write("\n" "\n" "Go light up the world, you glittering ray of sunshine!")
	    f.close()

        return
    
     #function that will enable the second NDVI parameter "NIR band" once "Red band" is satisfied
    def updateParameters(self, parameters):
        if(parameters[3].value):
	    parameters[4].enabled=True

    	return




