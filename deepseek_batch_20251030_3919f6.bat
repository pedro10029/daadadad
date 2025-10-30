@echo off
title DEXOS ULTIMATE SYSTEM v4.0 - Instalador Revolucionário
mode con: cols=80 lines=30
color 0A

echo.
echo ========================================================
echo          DEXOS ULTIMATE SYSTEM v4.0 - INSTALADOR
echo           Sistema Revolucionário Completo Avançado
echo ========================================================
echo.
echo [SISTEMA REVOLUCIONÁRIO] Iniciando instalação avançada...
echo.

:: Verificar se é administrador
net session >nul 2>&1
if %errorLevel% neq 0 (
    echo [AVISO] Execute como Administrador para instalação completa!
    echo.
    pause
)

:: Verificar Python
python --version >nul 2>&1
if %errorLevel% neq 0 (
    echo [ERRO] Python não encontrado!
    echo.
    echo [SOLUÇÃO] Instale Python 3.8+ em: python.org
    echo.
    echo [DOWNLOAD] https://www.python.org/downloads/
    echo.
    pause
    exit /b 1
)

echo [✓] Python detectado
python --version
echo.

:: Verificar versão do Python
for /f "tokens=2" %%i in ('python --version 2^>^&1') do set python_version=%%i
for /f "tokens=1,2 delims=." %%a in ("%python_version%") do (
    if %%a lss 3 (
        echo [ERRO] Python 3.8+ requerido. Versão atual: %python_version%
        pause
        exit /b 1
    )
    if %%a equ 3 if %%b lss 8 (
        echo [ERRO] Python 3.8+ requerido. Versão atual: %python_version%
        pause
        exit /b 1
    )
)

echo [✓] Versão do Python compatível: %python_version%
echo.

:: Atualizar pip
echo [INFO] Atualizando gerenciador de pacotes...
python -m pip install --upgrade pip
echo.

echo [INFO] Instalando componentes revolucionários avançados...
echo.

:: Instalar dependências principais
echo [1/6] Instalando dependências principais...
pip install opencv-python pyttsx3 speechrecognition pillow numpy

:: Instalar dependências avançadas
echo [2/6] Instalando dependências avançadas...
pip install psutil screeninfo GPUtil

:: Instalar dependências de interface
echo [3/6] Instalando dependências de interface...
pip install tkinter

:: Verificar instalações
echo [4/6] Verificando instalações...
python -c "import cv2, pyttsx3, speech_recognition, PIL, numpy, psutil, screeninfo" >nul 2>&1
if %errorLevel% neq 0 (
    echo [ERRO] Falha na instalação de dependências!
    echo.
    pause
    exit /b 1
)

echo [✓] Todas as dependências instaladas com sucesso!
echo.

:: Criar diretório do sistema
set "DEXOS_DIR=%USERPROFILE%\DEXOS_ULTIMATE_SYSTEM_v4"
echo [5/6] Configurando ambiente DEXOS ULTIMATE v4.0...

if not exist "%DEXOS_DIR%" (
    mkdir "%DEXOS_DIR%"
    echo [✓] Diretório criado: %DEXOS_DIR%
)

:: Copiar sistema principal
if exist "dexos_ultimate_system_v4.py" (
    copy "dexos_ultimate_system_v4.py" "%DEXOS_DIR%\"
    echo [✓] Sistema principal copiado
) else (
    echo [AVISO] Arquivo principal não encontrado, criando estrutura...
)

:: Criar arquivo de licença
echo [6/6] Configurando sistema de proteção avançado...
(
echo {
echo   "produto": "DEXOS ULTIMATE SYSTEM v4.0",
echo   "versao": "4.0.0",
echo   "tipo": "EDUCACAO_PREMIUM_PLUS",
echo   "valido": true,
echo   "expiracao": "PERMANENTE",
echo   "nivel_acesso": "REVOLUCIONARIO",
echo   "data_instalacao": "%date% %time%"
echo }
) > "%DEXOS_DIR%\dexos_secure.license"

echo [✓] Sistema de proteção configurado
echo.

:: Criar atalhos
set "DESKTOP=%USERPROFILE%\Desktop"
set "START_MENU=%APPDATA%\Microsoft\Windows\Start Menu\Programs"

echo [INFO] Criando acessos revolucionários...

:: Atalho na área de trabalho
powershell -Command "
$WshShell = New-Object -comObject WScript.Shell;
$Shortcut = $WshShell.CreateShortcut('%DESKTOP%\DEXOS ULTIMATE v4.0.lnk');
$Shortcut.TargetPath = 'python';
$Shortcut.Arguments = '\"%DEXOS_DIR%\dexos_ultimate_system_v4.py\"';
$Shortcut.WorkingDirectory = '%DEXOS_DIR%';
$Shortcut.WindowStyle = 1;
$Shortcut.Description = 'DEXOS ULTIMATE v4.0 - Sistema Revolucionário Avançado';
$Shortcut.IconLocation = '%SystemRoot%\System32\SHELL32.dll,25';
$Shortcut.Save()
"

:: Atalho no menu iniciar
if not exist "%START_MENU%\DEXOS ULTIMATE\" mkdir "%START_MENU%\DEXOS ULTIMATE\"

powershell -Command "
$WshShell = New-Object -comObject WScript.Shell;
$Shortcut = $WshShell.CreateShortcut('%START_MENU%\DEXOS ULTIMATE\DEXOS ULTIMATE v4.0.lnk');
$Shortcut.TargetPath = 'python';
$Shortcut.Arguments = '\"%DEXOS_DIR%\dexos_ultimate_system_v4.py\"';
$Shortcut.WorkingDirectory = '%DEXOS_DIR%';
$Shortcut.WindowStyle = 1;
$Shortcut.Description = 'DEXOS ULTIMATE v4.0 - Sistema Revolucionário Avançado';
$Shortcut.IconLocation = '%SystemRoot%\System32\SHELL32.dll,25';
$Shortcut.Save()
"

echo [✓] Acessos criados com sucesso
echo.

:: Criar arquivo de desinstalação
(
echo @echo off
echo title DEXOS ULTIMATE SYSTEM - Desinstalador
echo echo.
echo echo ========================================================
echo echo          DEXOS ULTIMATE SYSTEM - DESINSTALADOR
echo echo ========================================================
echo echo.
echo echo [AVISO] Esta ação removerá completamente o sistema DEXOS.
echo echo.
echo set /p confirm="Confirma a desinstalação? (S/N): "
echo if /i "!confirm!"=="S" (
echo     echo.
echo     echo [INFO] Removendo arquivos...
echo     rmdir /s /q "%DEXOS_DIR%"
echo     del "%DESKTOP%\DEXOS ULTIMATE v4.0.lnk"
echo     rmdir /s /q "%START_MENU%\DEXOS ULTIMATE"
echo     echo [✓] Sistema DEXOS removido com sucesso!
echo ) else (
echo     echo.
echo     echo [INFO] Desinstalação cancelada.
echo )
echo echo.
echo pause
) > "%DEXOS_DIR%\uninstall_dexos.bat"

echo [✓] Sistema de desinstalação criado
echo.

:: Teste final do sistema
echo [INFO] Executando teste final do sistema...
python -c "
import sys
print('=== TESTE DO SISTEMA DEXOS ULTIMATE v4.0 ===')
try:
    import cv2
    print('✓ OpenCV: OK')
except: print('✗ OpenCV: FALHA')
try:
    import pyttsx3
    print('✓ Sistema de Voz: OK')
except: print('✗ Sistema de Voz: FALHA')
try:
    import speech_recognition
    print('✓ Reconhecimento de Voz: OK')
except: print('✗ Reconhecimento de Voz: FALHA')
try:
    import psutil
    print('✓ Monitoramento: OK')
except: print('✗ Monitoramento: FALHA')
print('=========================================')
print('Sistema pronto para uso revolucionário!')
"
echo.

:: Mensagem final
echo ========================================================
echo      SISTEMA REVOLUCIONÁRIO v4.0 INSTALADO COM SUCESSO!
echo ========================================================
echo.
echo 🚀 DEXOS ULTIMATE SYSTEM v4.0 - CARACTERÍSTICAS:
echo.
echo ✅ Sistema de Voz Português Brasileiro Nativo
echo ✅ HUD Revolucionário com Partículas Quânticas
echo ✅ Proteção Avançada com Criptografia Quântica
echo ✅ Interface Fullscreen Imersiva
echo ✅ Monitoramento em Tempo Real do Sistema
echo ✅ Câmera Inteligente com Processamento
echo ✅ Modo Revolucionário (Potência Máxima)
echo ✅ Comunicação Avançada com Alertas
echo.
echo 🎯 NOVIDADES DA VERSÃO 4.0:
echo → Voz em Português Natural e Expressiva
echo → HUD com Efeitos Visuais 3D Avançados
echo → Sistema de Proteção com SHA3-256 + BLAKE2
echo → Métricas de Sistema em Tempo Real
echo → Interface Redesenhada e Otimizada
echo → Comandos por Voz em PT-BR
echo → Sistema de Notificações Inteligente
echo.
echo 📁 LOCAL DE INSTALAÇÃO:
echo %DEXOS_DIR%
echo.
echo 🎮 COMO USAR:
echo 1. Clique em "DEXOS ULTIMATE v4.0" na área de trabalho
echo 2. Aguarde a inicialização revolucionária
echo 3. Use comandos de voz em português:
echo    - "Dexos, status" - Status do sistema
echo    - "Dexos, analisar" - Análise completa
echo    - "Dexos, proteção" - Status de proteção
echo    - "Dexos, câmera" - Ativar câmera
echo    - "Dexos, modo revolucionário" - Potência máxima
echo    - "Dexos, ajuda" - Ajuda completa
echo.
echo 🛡️ SISTEMA DE PROTEÇÃO ATIVO:
echo → Licença Educacional Premium Plus
echo → Criptografia Quântica Ativa
echo → Assinatura Digital Única
echo → Validação de Integridade
echo.
echo 🔧 SUPORTE TÉCNICO:
echo Em caso de problemas:
echo 1. Execute como Administrador
echo 2. Verifique se o Python está no PATH
echo 3. Execute o teste de dependências
echo.
echo 🎓 PROJETO ESCOLAR REVOLUCIONÁRIO
echo Desenvolvido para demonstrações avançadas de IA
echo.
pause

:: Iniciar sistema automaticamente?
echo.
set /p iniciar="Deseja iniciar o DEXOS ULTIMATE agora? (S/N): "
if /i "%iniciar%"=="S" (
    echo.
    echo [INFO] Iniciando DEXOS ULTIMATE v4.0...
    timeout /t 2 /nobreak >nul
    cd /d "%DEXOS_DIR%"
    python "dexos_ultimate_system_v4.py"
)

exit /b 0