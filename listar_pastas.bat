@echo off
set "PastaRaiz=Definir o caminho da pasta raiz"
set "ArquivoSaida=%UserProfile%\Downloads\lista_pastas.txt"

echo Gerando lista de pastas (usando metodo moderno para OneDrive)...
echo Por favor, aguarde.

REM Verifica se o caminho raiz existe
if not exist "%PastaRaiz%" (
    echo ERRO: O caminho "%PastaRaiz%" nao foi encontrado.
    goto :fim
)

REM O PowerShell lida melhor com pastas "sob demanda" do OneDrive
(
    echo %PastaRaiz%
    powershell.exe -NoProfile -Command "Get-ChildItem -Path '%PastaRaiz%' -Recurse -Directory | Select-Object -ExpandProperty FullName"
) > "%ArquivoSaida%"

echo.
echo Concluido!
echo A lista de pastas foi salva em:
echo %ArquivoSaida%

:fim
echo.
echo Pressione qualquer tecla para sair...
pause