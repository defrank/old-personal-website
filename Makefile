###############################################################################
# $Id: Makefile,v 1.3 2013-05-24 15:40:36-07 dmf - $
# Derek Frank (dmfrank@gmx.com)
#
# NAME
#   Makefile
#
# DESCRIPTION
#   A common Makefile
#
###############################################################################

MKFILE          = Makefile
WHOAMI         ?= $(shell whoami)
PWD             = $(shell pwd)
CWD             = $(shell basename ${PWD})
#
# Define the "ci" command with respect to the current user.
# dmfrank, derekmfrank, dmf, ghoti, fain are all aliases.
#
CICMD           = ci
ifeq (${WHOAMI},dmf)
CICMD           = cil
endif

#
# Define checksource
#
CHK80           = checksource -l 80

#
# Variables
#

## DIRECTORIES
DIR_DJANGO      = mysite/mysite/
DIR_MEDIA       = public/media/
DIR_VIEWS       = ${DIR_DJANGO}views/
# Apps
DIR_APPS        = mysite/
DIR_TEMPLATES   = ${DIR_APPS}templates/
DIR_STATIC      = ${DIR_APPS}staticfiles/
DIR_IMG         = ${DIR_STATIC}img/
DIR_DOC         = ${DIR_STATIC}doc/
DIR_JS          = ${DIR_STATIC}js/
DIR_ICO         = ${DIR_STATIC}ico/
DIR_LOGO        = ${DIR_STATIC}css/navbar/
DIR_CSS         = ${DIR_STATIC}css/
DIR_WEBMASTER   = ${DIR_APPS}webmaster/

## DJANGO
VIEWFILES       = ${DIR_VIEWS}view_functions.py ${DIR_VIEWS}views.py
DJANGOFILES     = ${DIR_APPS}manage.py          ${DIR_DJANGO}settings.py       \
                  ${DIR_DJANGO}urls.py     ${DIR_DJANGO}context_processors.py  \
				  ${DIR_DJANGO}mysite.db        ${VIEWFILES} ${TEMPLATESFILES}

## APPS
APP_TEMPLATES   = ${DIR_TEMPLATES}__init__.py   ${DIR_TEMPLATES}urls.py        \
                  ${DIR_TEMPLATES}models.py     ${DIR_TEMPLATES}views.py       \
                  ${DIR_TEMPLATES}base.html     ${DIR_TEMPLATES}home.html      \
                  ${DIR_TEMPLATES}blog.html     ${DIR_TEMPLATES}portfolio.html \
                  ${DIR_TEMPLATES}aboutme.html  ${DIR_TEMPLATES}mff.html
## MEDIA/STATIC
IMGFILES        = ${DIR_IMG}favicon.ico         ${DIR_IMG}favicon.gif
DOCFILES        = 
JSFILES         = 
ICOFILES        = ${DIR_ICO}favicon.ico         ${DIR_ICO}favicon.gif
LOGOFILES       = 
CSSFILES        = ${DIR_CSS}style.css           ${DIR_CSS}navbar/navbar.css
STATICFILES     = 
APP_STATIC      = ${DIR_STATIC}__init__.py      ${DIR_STATIC}urls.py           \
                  ${DIR_STATIC}models.py        ${DIR_STATIC}views.py          \
                  ${CSSFILES} ${ICONFILES} ${LOGOFILES} ${IMGFILES} ${JSFILES} \
                  ${DOCFILES}
APP_WEBMASTER   = ${DIR_WEBMASTER}__init__.py   ${DIR_WEBMASTER}urls.py        \
				  ${DIR_WEBMASTER}views.py                                     \
				  ${DIR_WEBMASTER}templates/google0a2e75908547fa0e.html        \
				  ${DIR_WEBMASTER}templates/BingSiteAuth.xml
APPSFILES       = ${APP_TEMPLATES} ${APP_STATIC} ${APP_WEBMASTER}

## MISC
SERVFILES       = .htaccess
TXT             = README
FILES           =
CHKSRC          = ${MKFILE}
CHKFILES        =

## ALL
ALLFILES        = ${MKFILE}    ${TXT}        ${SERVFILES}  ${DJANGOFILES}      \
				  ${STATICFILES}             ${APPSFILES}

#
# make all
#
all : clean sync

#
# Run checksource on the files
#
check : ${CHKSRC}
	- ${CHK80} ${CHKSRC}

#
# Check files into an RCS subdirectory
#
ci :
ifeq (${WHOAMI},dmf)
	#rcs -U ${ALLFILES}
	${CICMD} + ${ALLFILES}
endif

#
# Initialize git repository
#
gitinit :
	touch README
	git init
	git add README Makefile
	git commit -m "First commit"
	git remote add origin git@bitbucket.org:dmfrank/${CWD}.git
	git push -u origin master

#
# Sync local and remote repositories
#
sync : ci
	git add --all
	git commit -a
	git status
	git push
#	git pull

#
# Clean and spotless remove genereated files
#
clean :
	- rm blah

spotless : clean
