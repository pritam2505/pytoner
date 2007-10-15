#include <stdio.h>
#include <windows.h>

#define DEFAULT_PYTHON_PATH "c:\\Python25\\python.exe"
#define STRING_LEN 1024

int WINAPI WinMain(HINSTANCE hInstance,HINSTANCE hPrevInstance,PSTR szCmdLine,int iCmdShow)
{
    char python_path[STRING_LEN];
    char command[STRING_LEN];
    
    GetPrivateProfileString("win32", "python", DEFAULT_PYTHON_PATH,
                            python_path, STRING_LEN - 1,
                            "./pytoner.cfg");
    snprintf(command, STRING_LEN - 1, "%s pytoner", python_path);
    system(command);
}
