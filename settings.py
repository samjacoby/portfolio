import os, sys
import logging
import logging.handlers

DEBUG = True

ROOT_PATH = os.path.abspath(os.path.dirname(__file__))
sys.path = [ROOT_PATH] + sys.path

#Directories
LAYOUT_DIR = os.path.join(ROOT_PATH, 'layout')
CONTENT_DIR = os.path.join(ROOT_PATH, 'content')
MEDIA_DIR = os.path.join(ROOT_PATH, 'media')
DEPLOY_DIR = os.path.join(ROOT_PATH, 'deploy')
TMP_DIR = os.path.join(ROOT_PATH, 'deploy_tmp')

BACKUPS_DIR = os.path.join(ROOT_PATH, 'backups')
BACKUP = False

LOG_DIR = os.path.join(ROOT_PATH, 'log')
LOG_NAME = 'portfolio.log'

SITE_ROOT = "/"
#SITE_ROOT = "/portfolio/"
SITE_WWW_URL = "http://shackmanpress.com/portfolio/"
SITE_NAME = "Sam Jacoby"
SITE_AUTHOR = "Sam Jacoby"

# Unicode
FILE_CHARSET = 'utf-8'

#Url Configuration
GENERATE_ABSOLUTE_FS_URLS = False

# Clean urls causes Hyde to generate urls without extensions. Examples:
# http://example.com/section/page.html becomes
# http://example.com/section/page/, and the listing for that section becomes
# http://example.com/section/
# The built-in CherryPy webserver is capable of serving pages with clean urls
# without any additional configuration, but Apache will need to use Mod_Rewrite
# to map the clean urls to the actual html files.  The HtaccessGenerator site
# post processor is capable of automatically generating the necessary
# RewriteRules for use with Apache.
GENERATE_CLEAN_URLS = True

# A list of filenames (without extensions) that will be considered listing
# pages for their enclosing folders.
# LISTING_PAGE_NAMES = ['index']
LISTING_PAGE_NAMES = ['listing', 'index', 'default']

# Determines whether or not to append a trailing slash to generated urls when
# clean urls are enabled.
APPEND_SLASH = True

# {folder : extension : (processors)}
# The processors are run in the given order and are chained.
# Only a lone * is supported as an indicator for folders. Path 
# should be specified. No wildcard card support yet.
 
# Starting under the media folder. For example, if you have media/css under 
# your site root,you should specify just css. If you have media/css/ie you 
# should specify css/ie for the folder name. css/* is not supported (yet).

# Extensions do not support wildcards.

MEDIA_PROCESSORS = {
    '*':{
        '.ccss':('hydeengine.media_processors.TemplateProcessor',
                'hydeengine.media_processors.CleverCSS',
                'hydeengine.media_processors.YUICompressor',),
        '.less':('hydeengine.media_processors.TemplateProcessor',
                'hydeengine.media_processors.LessCSS',
                'hydeengine.media_processors.YUICompressor',),                
        '.js':(
                'hydeengine.media_processors.TemplateProcessor',
                'hydeengine.media_processors.YUICompressor',)
    }, 
    'images/':{
        '.jpg':('hydeengine.media_processors.Thumbnail',),
        '.png':('hydeengine.media_processors.Thumbnail',)
        }
}

CONTENT_PROCESSORS = {
    'prerendered/': {
        '*.*' : 
            ('hydeengine.content_processors.PassthroughProcessor',)
            }
}

SITE_POST_PROCESSORS = {
    # 'media/js': {
    #        'hydeengine.site_post_processors.FolderFlattener' : {
    #                'remove_processed_folders': True,
    #                'pattern':"*.js"
    #        }
    #    }
}

CONTEXT = {
    'GENERATE_CLEAN_URLS': GENERATE_CLEAN_URLS
}

FILTER = { 
    'include': (".htaccess",),
    'exclude': (".*","*~")
}        


#Processor Configuration 

# 
#  Set this to the output of `which growlnotify`. If `which`  returns emtpy,
#  install growlnotify from the Extras package that comes with the Growl disk image.
# 
#
GROWL = None

# path for YUICompressor, or None if you don't
# want to compress JS/CSS. Project homepage:
# http://developer.yahoo.com/yui/compressor/
#YUI_COMPRESSOR = "./lib/yuicompressor-2.4.2.jar"
#YUI_COMPRESSOR = None                   
import yuicompressor
YUI_COMPRESSOR = os.path.join(os.path.dirname(yuicompressor.__file__), 'yuicompressor.jar')

# Path for LESSCSS
LESS_CSS_PATH = '/opt/local/bin/lessc'

# path for Closure Compiler, or None if you don't
# want to compress JS/CSS. Project homepage:
# http://closure-compiler.googlecode.com/
#CLOSURE_COMPILER = "./lib/compiler.jar"
CLOSURE_COMPRILER = None 

# path for HSS, which is a preprocessor for CSS-like files (*.hss)
# project page at http://ncannasse.fr/projects/hss
#HSS_PATH = "./lib/hss-1.0-osx"
HSS_PATH = None # if you don't want to use HSS


THUMBNAIL_MAX_WIDTH = 540                                                     
THUMBNAIL_MAX_HEIGHT = 1000                                                           
IMAGE_JPEG_QUALITY = 80

THUMBNAIL_FILENAME_POSTFIX = ''   

#Django settings

TEMPLATE_DIRS = (LAYOUT_DIR, CONTENT_DIR, TMP_DIR, MEDIA_DIR)

# Access time, filename/function#line-number message
log_formatter = logging.Formatter("[%(asctime)s %(filename)s/%(funcName)s#%(lineno)d] %(message)s")

INSTALLED_APPS = (
    'hydeengine',
    'django.contrib.webdesign',
#    'extensions'
)

# Add log setup after local imports
LOG_FILE = os.path.join(LOG_DIR, LOG_NAME)
try:
    if not os.path.exists(os.path.dirname(LOG_FILE)):
        os.mkdir(os.path.dirname(LOG_FILE))
    try:
        handler = logging.handlers.TimedRotatingFileHandler(filename=LOG_FILE, when='midnight')
        pass
    except IOError:
        # This is a permission error that occurs when running jobs as the ofps user via Fab
        # Instead of a unique file just send to stderr
        import sys
        handler = logging.StreamHandler(sys.stderr)
    handler.setFormatter(log_formatter)
    log = logging.getLogger('')
    if DEBUG:
        log.setLevel(logging.DEBUG)
    else:
        log.setLevel(logging.WARN)
    log.addHandler(handler)
except OSError:
    pass
