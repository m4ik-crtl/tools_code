@echo off
setlocal
:: Define a codificação para UTF-8 para aceitar acentos
chcp 65001 > nul


set "PastaRaiz=C:\Users\example\Downloads\pasta_desejada"
set "ArquivoSaida=%UserProfile%\Downloads\lista_pastas.txt"

echo Gerando lista de pastas (usando metodo moderno para OneDrive)...
echo Alvo: "%PastaRaiz%"
echo Por favor, aguarde...

:: Verifica se o caminho raiz existe
if not exist "%PastaRaiz%" (
    echo.
    echo ERRO CRITICO:
    echo A pasta "%PastaRaiz%" nao foi encontrada.
    echo Verifique se o caminho esta correto.
    goto :fim
)

:: O PowerShell lida melhor com pastas "sob demanda" do OneDrive
:: Adicionado -LiteralPath para evitar erros com caracteres especiais como []
(
    echo %PastaRaiz%
    powershell.exe -NoProfile -Command "Get-ChildItem -LiteralPath '%PastaRaiz%' -Recurse -Directory | Select-Object -ExpandProperty FullName"
) > "%ArquivoSaida%"

echo.
echo Concluido!
echo A lista de pastas foi salva em:
echo %ArquivoSaida%

:fim
echo.
pause
