#ifdef _WIN32
/* Addition things */

char *getpassphrase(const char *prompt);
int setenv(const char *name, const char *value, int overwrite);

/* At least Vista */
#ifndef _WIN32_WINNT
#define _WIN32_WINNT 0x0600
#endif

#if _MSC_VER < 1900
#define snprintf _snprintf
#endif
#define strcasecmp _stricmp
#define strncasecmp _strnicmp

/* Prevent inclusion of winsock.h in windows.h */

#define WIN32_LEAN_AND_MEAN 1

#include <windows.h>

/* avoid collision from min and max macros */

#undef min
#undef max


/* Temporary for debug */

//#undef DEBUG_LOG_STDERR
//#define DEBUG_LOG_STDERR 1

/* To avoid unsafe warnings (off) */

// #pragma warning(disable: 4996)
#endif