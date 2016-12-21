################################################################################
#
# FILE NAME: CommonConfig.py
#
# DESCRIPTION: This script contains common script configuration parameters for Leda
#              Test Suite
#
################################################################################

#######################################################################################################
# CREDENTIALS
#######################################################################################################
AccessKeyID = 'LTAIbY4B7xu5VuKB'
AccessKeySecret = 'Tdxf0ijim1fAIG9cgSpw1WCAVWOHhk'

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
#Throughput summary file name
###################################################################################################
summary_file = {'AliyunQuery':'AliyunQuery'}

###################################################################################################
#Throughtput results
###################################################################################################
results = {'AliyunQuery':'summary'}

###################################################################################################
#Throughput fieldname
###################################################################################################
results_field = {'AliyunQuery':'results'}
#################################################################################################
#time fieldname
#################################################################################################
start_time = {'AliyunQuery':'Start time'}
