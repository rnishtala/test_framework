################################################################################
#
# FILE NAME: CommonConfig.py
#
# DESCRIPTION: This script contains common script configuration parameters for Leda
#              Test Suite
#
################################################################################

from collections import namedtuple
#######################################################################################################
# CREDENTIALS
#######################################################################################################
AccessKeyID = '#####'
AccessKeySecret = '#####'


######################################################################################################
# Services
######################################################################################################
ServiceInfo = namedtuple('ServiceInfo', 'name, url, version, in_region, in_zone')
SERVICES = {"ram": ServiceInfo("ram", "https://ram.aliyuncs.com", "2015-05-01", True, False),
            "cms": ServiceInfo("cms", "http://metrics.aliyuncs.com", "2016-03-18", True, False),
            "ecs": ServiceInfo("ecs", "http://ecs.aliyuncs.com", "2014-05-26", True, True),
            "rds": ServiceInfo("rds", "http://rds.aliyuncs.com", "2014-08-15", True, True),
            "slb": ServiceInfo("slb", "http://slb.aliyuncs.com", "2014-05-15", True, False)}

#####################################################################################################
# (RegionId,InstanceId)
#####################################################################################################
hosts = [('us-west-1b', 'i-rj92o440hd7lpp198d18')]

LinPC = {'hostname':'ubuntu-dls-test'}

#############################################################################################################
# Log Params (follows python logging)
#############################################################################################################
VALID_LOG_LEVELS = [1, 2, 3, 4, 5]
# 1 = CRITICAL
# 2 = ERROR
# 3 = WARNING
# 4 = INFO
# 5 = DEBUG
CURR_LOG_LEVEL = 5
LOG_FILE_LOCATION = '/var/log/leda/ftp/' # Change this will not create the directory structure
#############################################################################################################

# Pattern from REGULAR EXPRESSION COOKBOOK by JAN GOYVAERTS, STEVEN LEVITHAN, page 379
ipv4_pattern = "^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
# Pattern from REGULAR EXPRESSION COOKBOOK by JAN GOYVAERTS, STEVEN LEVITHAN, page 388
ipv6_pattern = "^(?:(?:(?:[A-F0-9]{1,4}:){6}|(?=(?:[A-F0-9]{0,4}:){0,6}(?:[0-9]{1,3}\.){3}[0-9]{1,3}$)(([0-9A-F]{1,4}:){0,5}|:)((:[0-9A-F]{1,4}){1,5}:|:))(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)|(?:[A-F0-9]{1,4}:){7}[A-F0-9]{1,4}|(?=(?:[A-F0-9]{0,4}:){0,7}[A-F0-9]{0,4}$)(([0-9A-F]{1,4}:){1,7}|:)((:[0-9A-F]{1,4}){1,7}|:))$"


###################################################################################################
# LOAD TEST directory names
###################################################################################################
TEST = {'AliyunQuery':'./AliyunQuery/'}

###################################################################################################
# summary file name
###################################################################################################
summary_file = {'AliyunQuery':'AliyunQuery'}

###################################################################################################
#results
###################################################################################################
results = {'AliyunQuery':'summary'}

###################################################################################################
#fieldname
###################################################################################################
results_field = {'AliyunQuery':'results'}
#################################################################################################
#time fieldname
#################################################################################################
start_time = {'AliyunQuery':'Start time'}
