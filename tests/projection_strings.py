"""
Projection Strings for Testing
"""

# NOTE! interior quotes need to be double quotes to make esri happy

WGS_1984_UTM_Zone_23N = (
    """PROJCS["WGS_1984_UTM_Zone_23N","""
    """GEOGCS["GCS_WGS_1984","""
    """DATUM["D_WGS_1984","""
    """SPHEROID["WGS_1984",6378137.0,298.257223563]],"""
    """PRIMEM["Greenwich",0.0],"""
    """UNIT["Degree",0.0174532925199433]],"""
    """PROJECTION["Transverse_Mercator"],"""
    """PARAMETER["False_Easting",500000.0],"""
    """PARAMETER["False_Northing",0.0],"""
    """PARAMETER["Central_Meridian",-45.0],"""
    """PARAMETER["Scale_Factor",0.9996],"""
    """PARAMETER["Latitude_Of_Origin",0.0],"""
    """UNIT["Meter",1.0]];IsHighPrecision""")