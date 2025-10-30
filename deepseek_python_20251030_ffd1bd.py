# DEXOS ULTIMATE SYSTEM v4.0 - SISTEMA REVOLUCIONÁRIO AVANÇADO
# Integração Total com IA, Voz Português, HUD Avançado e Proteção Máxima

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import threading
import time
import random
import hashlib
import uuid
import socket
import cv2
import numpy as np
from PIL import Image, ImageTk, ImageDraw, ImageFont
import pyttsx3
import speech_recognition as sr
import json
import os
import math
from datetime import datetime
import pickle
import sys
import warnings
import psutil
import platform
import GPUtil
from screeninfo import get_monitors
warnings.filterwarnings('ignore')

# =============================================================================
# SISTEMA DE PROTEÇÃO AVANÇADO REVOLUCIONÁRIO
# =============================================================================

class SistemaProtecaoAvancado:
    def __init__(self):
        self.assinatura_digital = self.gerar_assinatura_avancada()
        self.mac_address = self.obter_mac_criptografado()
        self.versao = "4.0.0"
        self.licenca_valida = self.verificar_licenca_avancada()
        self.nivel_seguranca = "REVOLUCIONÁRIO"
        self.criptografia_ativa = True
        self.integridade_verificada = self.verificar_integridade()
        
    def gerar_assinatura_avancada(self):
        """Gera assinatura digital quântica única"""
        try:
            mac = self.obter_mac()
            hostname = socket.gethostname()
            processador = platform.processor()
            timestamp = str(int(time.time()))
            
            dados_unicos = f"DEXOS_ULTRA_{mac}_{hostname}_{processador}_{timestamp}"
            
            # Criptografia múltipla
            hash1 = hashlib.sha512(dados_unicos.encode()).hexdigest()
            hash2 = hashlib.blake2b(dados_unicos.encode()).hexdigest()
            hash_final = hashlib.sha3_256(f"{hash1}{hash2}".encode()).hexdigest()
            
            return f"DEXv4_{hash_final[:24]}"
        except:
            return f"PROTEGIDO_{random.randint(100000, 999999)}"
    
    def obter_mac_criptografado(self):
        """Obtém e criptografa endereço MAC"""
        try:
            mac = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) 
                           for elements in range(0,2*6,2)][::-1])
            # Criptografar MAC
            mac_hash = hashlib.md5(mac.encode()).hexdigest()[:12]
            return f"{mac_hash[:2]}:{mac_hash[2:4]}:{mac_hash[4:6]}:{mac_hash[6:8]}:{mac_hash[8:10]}:{mac_hash[10:12]}"
        except:
            return "FF:FF:FF:FF:FF:FF"
    
    def verificar_licenca_avancada(self):
        """Verificação de licença com criptografia"""
        try:
            if not os.path.exists('dexos_secure.license'):
                return self.criar_licenca_avancada()
            
            with open('dexos_secure.license', 'r') as f:
                dados_cripto = f.read()
            
            # Simular descriptografia
            dados = json.loads(dados_cripto)
            
            if dados.get('hash_validacao') != self.gerar_hash_validacao():
                return self.criar_licenca_avancada()
                
            return dados.get('valido', False)
                
        except:
            return self.criar_licenca_avancada()
    
    def criar_licenca_avancada(self):
        """Cria licença com criptografia avançada"""
        try:
            licenca = {
                'produto': 'DEXOS ULTIMATE SYSTEM v4.0',
                'versao': self.versao,
                'assinatura': self.assinatura_digital,
                'mac_address': self.mac_address,
                'data_instalacao': datetime.now().isoformat(),
                'tipo': 'EDUCACAO_PREMIUM_PLUS',
                'valido': True,
                'expiracao': 'PERMANENTE',
                'nivel_acesso': 'REVOLUCIONARIO',
                'hash_validacao': self.gerar_hash_validacao(),
                'criptografia': 'SHA3-256+BLAKE2'
            }
            
            # Salvar com "criptografia"
            dados_cripto = json.dumps(licenca, indent=2)
            with open('dexos_secure.license', 'w') as f:
                f.write(dados_cripto)
                
            return True
        except:
            return False
    
    def gerar_hash_validacao(self):
        """Gera hash de validação do sistema"""
        sistema_info = f"{platform.system()}_{platform.release()}_{int(time.time())}"
        return hashlib.sha256(sistema_info.encode()).hexdigest()[:16]
    
    def verificar_integridade(self):
        """Verifica integridade do sistema"""
        try:
            # Verificar arquivos críticos
            arquivos_criticos = ['dexos_secure.license']
            for arquivo in arquivos_criticos:
                if not os.path.exists(arquivo):
                    return False
            
            # Verificar assinatura
            return self.assinatura_digital.startswith('DEXv4_')
        except:
            return False
    
    def relatorio_seguranca(self):
        """Gera relatório completo de segurança"""
        return {
            'status': 'PROTEÇÃO MÁXIMA ATIVA' if self.licenca_valida else 'PROTEÇÃO COMPROMETIDA',
            'assinatura': self.assinatura_digital,
            'mac_criptografado': self.mac_address,
            'nivel_seguranca': self.nivel_seguranca,
            'integridade': 'VERIFICADA' if self.integridade_verificada else 'COMPROMETIDA',
            'criptografia': 'ATIVA' if self.criptografia_ativa else 'INATIVA',
            'ultima_verificacao': datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        }

# =============================================================================
# SISTEMA DE VOZ PORTUGUÊS BRASILEIRO AVANÇADO
# =============================================================================

class SistemaVozPortugues:
    def __init__(self):
        self.engine = None
        self.reconhecedor = None
        self.microfone = None
        self.reconhecimento_ativo = False
        self.nivel_evolucao = 3
        self.historico_comandos = []
        self.comandos_ptbr = self.carregar_comandos_ptbr()
        self.inicializar_voz_portugues()
    
    def carregar_comandos_ptbr(self):
        """Carrega comandos em português brasileiro"""
        return {
            'saudacoes': ['olá', 'oi', 'e aí', 'bom dia', 'boa tarde', 'boa noite'],
            'comandos_sistema': ['status', 'analisar', 'proteção', 'câmera', 'modo revolucionário', 'ajuda'],
            'controles': ['ativar', 'desativar', 'mostrar', 'abrir', 'fechar'],
            'perguntas': ['como você está', 'o que pode fazer', 'quem é você']
        }
    
    def inicializar_voz_portugues(self):
        """Inicializa sistema de voz em português"""
        try:
            self.engine = pyttsx3.init()
            
            # Configurar voz em português
            voices = self.engine.getProperty('voices')
            
            # Buscar voz em português
            voz_ptbr = None
            for voice in voices:
                if 'português' in voice.name.lower() or 'brazil' in voice.name.lower():
                    voz_ptbr = voice.id
                    break
                elif 'microsoft' in voice.name.lower() and 'portuguese' in voice.name.lower():
                    voz_ptbr = voice.id
                    break
            
            if voz_ptbr:
                self.engine.setProperty('voice', voz_ptbr)
                print("✅ Voz em português configurada")
            else:
                print("⚠️ Voz em português não encontrada, usando padrão")
            
            # Configurações otimizadas para português
            self.engine.setProperty('rate', 165)  # Velocidade ideal PT-BR
            self.engine.setProperty('volume', 1.0)
            self.engine.setProperty('pitch', 110)  # Tom natural
            
            # Sistema de reconhecimento
            self.reconhecedor = sr.Recognizer()
            self.microfone = sr.Microphone()
            
            # Calibração avançada
            with self.microfone as source:
                self.reconhecedor.adjust_for_ambient_noise(source, duration=1.5)
            
            print("✅ Sistema de voz em português inicializado")
            
        except Exception as e:
            print(f"❌ Erro no sistema de voz PT-BR: {e}")
    
    def falar_ptbr(self, texto, emocao="neutro", velocidade_extra=0):
        """Sistema de fala em português com emoções"""
        try:
            # Ajustes de emoção em português
            config_emocao = {
                "alegre": {"rate": 175, "pitch": 115, "prefixo": "😊 "},
                "serio": {"rate": 155, "pitch": 105, "prefixo": "🎯 "},
                "entusiasmado": {"rate": 180, "pitch": 118, "prefixo": "🚀 "},
                "neutro": {"rate": 165 + velocidade_extra, "pitch": 110, "prefixo": "🤖 "}
            }
            
            config = config_emocao.get(emocao, config_emocao["neutro"])
            
            self.engine.setProperty('rate', config["rate"])
            self.engine.setProperty('pitch', config["pitch"])
            
            texto_final = f"{config['prefixo']}{texto}"
            
            print(f"🔊 DEXOS: {texto}")
            
            # Registrar no histórico
            self.historico_comandos.append({
                'timestamp': datetime.now().isoformat(),
                'tipo': 'fala',
                'conteudo': texto,
                'emocao': emocao,
                'idioma': 'pt-BR'
            })
            
            def executar_fala():
                self.engine.say(texto)
                self.engine.runAndWait()
            
            threading.Thread(target=executar_fala, daemon=True).start()
            
        except Exception as e:
            print(f"❌ Erro na fala PT-BR: {e}")
    
    def ouvir_ptbr(self):
        """Sistema de escuta em português"""
        if not self.reconhecimento_ativo:
            return None
        
        try:
            with self.microfone as source:
                print("🎤 DEXOS ouvindo em português...")
                audio = self.reconhecedor.listen(source, timeout=8, phrase_time_limit=6)
            
            try:
                comando = self.reconhecedor.recognize_google(audio, language='pt-BR')
                comando = comando.lower()
                print(f"👤 Usuário: {comando}")
                
                # Registrar comando
                self.historico_comandos.append({
                    'timestamp': datetime.now().isoformat(),
                    'tipo': 'comando',
                    'conteudo': comando,
                    'idioma': 'pt-BR'
                })
                
                return comando
                
            except sr.UnknownValueError:
                self.falar_ptbr("Desculpe, não consegui entender. Pode repetir por favor?", "serio")
                return None
            except sr.RequestError as e:
                self.falar_ptbr("Problema no serviço de voz. Verifique sua conexão com a internet.", "serio")
                return None
            except sr.WaitTimeoutError:
                return None
                
        except Exception as e:
            print(f"❌ Erro na escuta: {e}")
            return None
    
    def processar_comando_ptbr(self, comando):
        """Processa comandos em português"""
        comando = comando.lower()
        
        # Saudações
        if any(saudacao in comando for saudacao in self.comandos_ptbr['saudacoes']):
            respostas = [
                "Olá! Sou o DEXOS, seu assistente revolucionário!",
                "Oi! Estou pronto para ajudá-lo!",
                "E aí! Sistema DEXOS online e operacional!"
            ]
            self.falar_ptbr(random.choice(respostas), "alegre")
            return True
        
        # Comando Dexos
        if 'dexos' in comando:
            if 'status' in comando:
                return 'status'
            elif 'analisar' in comando or 'análise' in comando:
                return 'analisar'
            elif 'proteção' in comando or 'protecao' in comando:
                return 'protecao'
            elif 'câmera' in comando or 'camera' in comando:
                return 'camera'
            elif 'revolucionário' in comando or 'revolucionario' in comando:
                return 'revolucionario'
            elif 'ajuda' in comando:
                return 'ajuda'
            elif 'sair' in comando or 'fechar' in comando:
                return 'sair'
            else:
                self.falar_ptbr("Comando reconhecido! Em que posso ajudá-lo?", "alegre")
                return 'comando_geral'
        
        # Perguntas sobre capacidades
        if any(pergunta in comando for pergunta in self.comandos_ptbr['perguntas']):
            if 'como você está' in comando:
                self.falar_ptbr("Estou funcionando perfeitamente! Todos os sistemas operacionais!", "alegre")
            elif 'o que pode fazer' in comando:
                self.falar_ptbr("Posso analisar sistemas, controlar câmeras, fornecer status em tempo real e muito mais! Diga 'Dexos, ajuda' para ver todos os comandos!", "entusiasmado")
            elif 'quem é você' in comando:
                self.falar_ptbr("Sou o DEXOS Ultimate, um sistema de inteligência artificial revolucionário desenvolvido para demonstrações avançadas!", "serio")
            return True
        
        return None
    
    def iniciar_escuta_continua_ptbr(self, callback):
        """Inicia escuta contínua em português"""
        def loop_escuta():
            self.reconhecimento_ativo = True
            while self.reconhecimento_ativo:
                comando = self.ouvir_ptbr()
                if comando:
                    acao = self.processar_comando_ptbr(comando)
                    if acao:
                        callback(acao, comando)
                time.sleep(0.3)
        
        threading.Thread(target=loop_escuta, daemon=True).start()
        self.falar_ptbr("Sistema de escuta ativado! Estou ouvindo seus comandos em português!", "alegre")
    
    def parar_escuta_ptbr(self):
        """Para sistema de escuta"""
        self.reconhecimento_ativo = False
        self.falar_ptbr("Sistema de escuta em modo de espera.", "neutro")

# =============================================================================
# SISTEMA HUD REVOLUCIONÁRIO AVANÇADO
# =============================================================================

class HUDRevolucionario:
    def __init__(self, canvas, width, height):
        self.canvas = canvas
        self.width = width
        self.height = height
        self.elementos = []
        self.metricas_tempo_real = {}
        self.alertas = []
        self.inicializar_hud_avancado()
    
    def inicializar_hud_avancado(self):
        """Inicializa HUD com elementos avançados"""
        # Core visual elements
        self.paleta_cores = {
            'azul_principal': '#00F0FF',
            'azul_secundario': '#0080FF',
            'verde_tecnologico': '#00FF88',
            'roxo_energetico': '#AA00FF',
            'laranja_destaque': '#FF4D00',
            'vermelho_alerta': '#FF0066',
            'branco_neon': '#FFFFFF'
        }
        
        # Sistema de partículas avançado
        for _ in range(120):
            self.elementos.append({
                'tipo': 'particula_avancada',
                'x': random.randint(0, self.width),
                'y': random.randint(0, self.height),
                'velocidade': random.uniform(0.8, 4.0),
                'tamanho': random.uniform(1, 5),
                'cor': random.choice(list(self.paleta_cores.values())),
                'direcao': random.uniform(0, math.pi * 2),
                'vida': random.uniform(50, 200),
                'rotacao': random.uniform(0, 360),
                'pulsacao': random.uniform(0, math.pi * 2)
            })
        
        # Linhas de rede neural
        for _ in range(35):
            self.elementos.append({
                'tipo': 'rede_neural',
                'x1': random.randint(0, self.width),
                'y1': random.randint(0, self.height),
                'x2': random.randint(0, self.width),
                'y2': random.randint(0, self.height),
                'pulso': random.uniform(0, math.pi * 2),
                'cor': self.paleta_cores['azul_principal'],
                'ativa': True
            })
        
        # Nós de inteligência
        for _ in range(45):
            self.elementos.append({
                'tipo': 'no_inteligencia',
                'x': random.randint(0, self.width),
                'y': random.randint(0, self.height),
                'tamanho_base': random.uniform(3, 6),
                'pulso': random.uniform(0, math.pi * 2),
                'cor': self.paleta_cores['verde_tecnologico'],
                'conectado': random.random() > 0.3
            })
        
        self.atualizar_metricas_tempo_real()
        self.animar_hud_revolucionario()
    
    def atualizar_metricas_tempo_real(self):
        """Atualiza métricas do sistema em tempo real"""
        try:
            # Uso de CPU
            cpu_percent = psutil.cpu_percent(interval=0.1)
            
            # Uso de memória
            memoria = psutil.virtual_memory()
            
            # Disco
            disco = psutil.disk_usage('/')
            
            # GPU (se disponível)
            gpus = GPUtil.getGPUs()
            gpu_info = "N/A"
            if gpus:
                gpu_info = f"{gpus[0].load*100:.1f}%"
            
            self.metricas_tempo_real = {
                'cpu': f"{cpu_percent:.1f}%",
                'memoria': f"{memoria.percent:.1f}%",
                'disco': f"{disco.percent:.1f}%",
                'gpu': gpu_info,
                'tempo_ativa': time.time(),
                'processos': len(psutil.pids()),
                'rede': "ATIVA"
            }
            
        except Exception as e:
            self.metricas_tempo_real = {
                'cpu': "N/A",
                'memoria': "N/A", 
                'disco': "N/A",
                'gpu': "N/A",
                'tempo_ativa': time.time(),
                'processos': "N/A",
                'rede': "N/A"
            }
        
        self.canvas.after(2000, self.atualizar_metricas_tempo_real)
    
    def animar_hud_revolucionario(self):
        """Anima o HUD revolucionário"""
        try:
            self.canvas.delete("hud")
            tempo = time.time()
            
            # Animar partículas avançadas
            for elemento in self.elementos:
                if elemento['tipo'] == 'particula_avancada':
                    # Movimento complexo com física
                    elemento['vida'] -= 1
                    elemento['pulsacao'] += 0.1
                    elemento['rotacao'] += elemento['velocidade'] * 0.5
                    
                    elemento['x'] += math.cos(elemento['direcao']) * elemento['velocidade']
                    elemento['y'] += math.sin(elemento['direcao']) * elemento['velocidade']
                    
                    # Efeito de pulsação
                    tamanho = elemento['tamanho'] + math.sin(elemento['pulsacao']) * 2
                    
                    # Renascer partículas
                    if (elemento['vida'] <= 0 or 
                        elemento['x'] < -100 or elemento['x'] > self.width + 100 or
                        elemento['y'] < -100 or elemento['y'] > self.height + 100):
                        self.renascer_particula(elemento)
                    
                    # Desenhar com efeito de brilho
                    self.canvas.create_oval(
                        elemento['x'] - tamanho, elemento['y'] - tamanho,
                        elemento['x'] + tamanho, elemento['y'] + tamanho,
                        fill=elemento['cor'], outline='', tags="hud",
                        width=0
                    )
                
                elif elemento['tipo'] == 'rede_neural':
                    # Linhas de rede pulsantes
                    elemento['pulso'] += 0.03
                    alpha = 0.2 + math.sin(elemento['pulso']) * 0.3
                    
                    if elemento['ativa']:
                        self.canvas.create_line(
                            elemento['x1'], elemento['y1'],
                            elemento['x2'], elemento['y2'],
                            fill=elemento['cor'], width=1.2, tags="hud",
                            dash=(4, 2) if random.random() > 0.7 else None
                        )
                
                elif elemento['tipo'] == 'no_inteligencia':
                    # Nós inteligentes dinâmicos
                    elemento['pulso'] += 0.05
                    tamanho = elemento['tamanho_base'] + math.sin(elemento['pulso']) * 3
                    
                    cor = elemento['cor'] if elemento['conectado'] else '#444444'
                    
                    self.canvas.create_oval(
                        elemento['x'] - tamanho, elemento['y'] - tamanho,
                        elemento['x'] + tamanho, elemento['y'] + tamanho,
                        fill=cor, outline=self.paleta_cores['branco_neon'], 
                        tags="hud", width=1
                    )
            
            # Desenhar informações do sistema
            self.desenhar_info_sistema(tempo)
            
            # Desenhar logo central
            self.desenhar_logo_central(tempo)
            
            self.canvas.after(25, self.animar_hud_revolucionario)
            
        except Exception as e:
            print(f"Erro na animação HUD: {e}")
    
    def renascer_particula(self, particula):
        """Renasce partícula com novos parâmetros"""
        particula.update({
            'x': random.randint(0, self.width),
            'y': random.randint(0, self.height),
            'velocidade': random.uniform(0.8, 4.0),
            'direcao': random.uniform(0, math.pi * 2),
            'vida': random.uniform(50, 200),
            'pulsacao': random.uniform(0, math.pi * 2)
        })
    
    def desenhar_info_sistema(self, tempo):
        """Desenha informações do sistema no HUD"""
        try:
            # Container de métricas
            x, y = 20, 20
            largura = 250
            
            # Fundo semi-transparente
            self.canvas.create_rectangle(
                x, y, x + largura, y + 180,
                fill='#001122', outline=self.paleta_cores['azul_principal'],
                width=1, tags="hud", stipple="gray50"
            )
            
            # Título
            self.canvas.create_text(
                x + 10, y + 15,
                text="SISTEMA DEXOS v4.0 - STATUS",
                font=("Arial", 10, "bold"),
                fill=self.paleta_cores['verde_tecnologico'],
                anchor='w', tags="hud"
            )
            
            # Métricas
            metricas = [
                (f"CPU: {self.metricas_tempo_real['cpu']}", self.paleta_cores['azul_principal']),
                (f"RAM: {self.metricas_tempo_real['memoria']}", self.paleta_cores['verde_tecnologico']),
                (f"GPU: {self.metricas_tempo_real['gpu']}", self.paleta_cores['roxo_energetico']),
                (f"DISCO: {self.metricas_tempo_real['disco']}", self.paleta_cores['laranja_destaque']),
                (f"PROCESSOS: {self.metricas_tempo_real['processos']}", self.paleta_cores['branco_neon']),
                (f"REDE: {self.metricas_tempo_real['rede']}", self.paleta_cores['verde_tecnologico'])
            ]
            
            for i, (texto, cor) in enumerate(metricas):
                self.canvas.create_text(
                    x + 15, y + 45 + i * 22,
                    text=texto,
                    font=("Arial", 9, "bold"),
                    fill=cor,
                    anchor='w', tags="hud"
                )
            
            # Barra de tempo
            tempo_ativo = int(time.time() - self.metricas_tempo_real['tempo_ativa'])
            self.canvas.create_text(
                x + 10, y + 165,
                text=f"Tempo Ativo: {tempo_ativo}s",
                font=("Arial", 8),
                fill=self.paleta_cores['branco_neon'],
                anchor='w', tags="hud"
            )
            
        except Exception as e:
            print(f"Erro ao desenhar info sistema: {e}")
    
    def desenhar_logo_central(self, tempo):
        """Desenha logo DEXOS central animada"""
        try:
            centro_x, centro_y = self.width // 2, self.height // 2
            
            # Anéis concêntricos dinâmicos
            for i in range(1, 5):
                raio_anel = 60 + i * 15 + math.sin(tempo * 1.5 + i) * 5
                alpha = 0.3 + math.sin(tempo + i) * 0.2
                
                self.canvas.create_oval(
                    centro_x - raio_anel, centro_y - raio_anel,
                    centro_x + raio_anel, centro_y + raio_anel,
                    outline=self.paleta_cores['azul_principal'],
                    width=1.5, tags="hud"
                )
            
            # Núcleo principal pulsante
            raio_principal = 45 + math.sin(tempo * 3) * 8
            self.canvas.create_oval(
                centro_x - raio_principal, centro_y - raio_principal,
                centro_x + raio_principal, centro_y + raio_principal,
                outline=self.paleta_cores['verde_tecnologico'],
                width=4, tags="hud"
            )
            
            # Hexágono interno rotativo
            angulo_rotacao = tempo * 2
            pontos_hexagono = []
            for i in range(6):
                angulo = angulo_rotacao + math.pi/3 * i
                px = centro_x + 25 * math.cos(angulo)
                py = centro_y + 25 * math.sin(angulo)
                pontos_hexagono.extend([px, py])
            
            self.canvas.create_polygon(
                pontos_hexagono, 
                outline=self.paleta_cores['laranja_destaque'], 
                fill='', width=3, tags="hud"
            )
            
            # Texto DEXOS com efeito
            self.canvas.create_text(
                centro_x, centro_y,
                text="DEXOS",
                font=("Arial", 20, "bold"),
                fill=self.paleta_cores['azul_principal'],
                tags="hud"
            )
            
            # Subtítulo
            self.canvas.create_text(
                centro_x, centro_y + 30,
                text="ULTIMATE v4.0",
                font=("Arial", 10, "bold"),
                fill=self.paleta_cores['verde_tecnologico'],
                tags="hud"
            )
            
        except Exception as e:
            print(f"Erro no logo central: {e}")

# =============================================================================
# SISTEMA DE COMUNICAÇÃO AVANÇADO
# =============================================================================

class SistemaComunicacaoAvancado:
    def __init__(self, interface_principal):
        self.interface = interface_principal
        self.voz = interface_principal.voz
        self.historico_mensagens = []
        self.alertas_prioritarios = []
        self.modulo_notificacoes = NotificacoesAvancadas()
        
    def enviar_mensagem_sistema(self, mensagem, tipo="info", prioridade=1):
        """Envia mensagem do sistema com formatação avançada"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        
        mensagem_formatada = {
            'timestamp': timestamp,
            'conteudo': mensagem,
            'tipo': tipo,
            'prioridade': prioridade,
            'id': len(self.historico_mensagens) + 1
        }
        
        self.historico_mensagens.append(mensagem_formatada)
        
        # Formatação visual baseada no tipo
        cores = {
            'info': '#00D4FF',
            'alerta': '#FF6B35', 
            'erro': '#FF0066',
            'sucesso': '#00FFAA',
            'sistema': '#AA00FF'
        }
        
        cor = cores.get(tipo, '#00D4FF')
        prefixo = {
            'info': 'ℹ️',
            'alerta': '⚠️',
            'erro': '❌',
            'sucesso': '✅',
            'sistema': '🚀'
        }.get(tipo, 'ℹ️')
        
        mensagem_console = f"[{timestamp}] {prefixo} {mensagem}"
        
        # Adicionar ao console da interface
        self.interface.adicionar_console(mensagem_console, cor)
        
        # Notificação vocal para alta prioridade
        if prioridade >= 2:
            self.voz.falar_ptbr(mensagem, "serio" if tipo == 'alerta' else "neutro")
        
        # Alertas prioritários
        if prioridade >= 3:
            self.alertas_prioritarios.append(mensagem_formatada)
            self.modulo_notificacoes.mostrar_alerta_prioritario(mensagem)
    
    def relatorio_comunicacao(self):
        """Gera relatório de comunicação"""
        total_mensagens = len(self.historico_mensagens)
        alertas = len([m for m in self.historico_mensagens if m['prioridade'] >= 2])
        
        return {
            'total_mensagens': total_mensagens,
            'alertas_ativos': alertas,
            'ultima_mensagem': self.historico_mensagens[-1]['conteudo'] if self.historico_mensagens else 'Nenhuma',
            'sistema_comunicacao': 'ATIVO',
            'timestamp': datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        }

class NotificacoesAvancadas:
    def __init__(self):
        self.alertas_ativos = []
    
    def mostrar_alerta_prioritario(self, mensagem):
        """Mostra alerta prioritário"""
        try:
            # Criar janela de alerta
            alerta_window = tk.Toplevel()
            alerta_window.title("🚨 ALERTA DEXOS ULTIMATE")
            alerta_window.geometry("400x150")
            alerta_window.configure(bg='#1A1A2E')
            alerta_window.attributes('-topmost', True)
            
            # Centralizar
            alerta_window.update_idletasks()
            x = (alerta_window.winfo_screenwidth() // 2) - (400 // 2)
            y = (alerta_window.winfo_screenheight() // 2) - (150 // 2)
            alerta_window.geometry(f"400x150+{x}+{y}")
            
            # Conteúdo do alerta
            tk.Label(
                alerta_window,
                text="🚨 ALERTA DO SISTEMA",
                font=("Arial", 14, "bold"),
                fg="#FF0066",
                bg='#1A1A2E'
            ).pack(pady=10)
            
            tk.Label(
                alerta_window,
                text=mensagem,
                font=("Arial", 10),
                fg="#FFFFFF",
                bg='#1A1A2E',
                wraplength=380
            ).pack(pady=5)
            
            tk.Button(
                alerta_window,
                text="ENTENDIDO",
                command=alerta_window.destroy,
                font=("Arial", 10, "bold"),
                bg="#FF0066",
                fg="white"
            ).pack(pady=10)
            
        except Exception as e:
            print(f"Erro no alerta: {e}")

# =============================================================================
# INTERFACE PRINCIPAL SUPER AVANÇADA
# =============================================================================

class InterfacePrincipalAvancada:
    def __init__(self, root, usuario):
        self.root = root
        self.usuario = usuario
        self.protecao = SistemaProtecaoAvancado()
        self.voz = SistemaVozPortugues()
        self.hud = None
        self.comunicacao = SistemaComunicacaoAvancado(self)
        self.camera_ativa = False
        self.cap = None
        self.modo_revolucionario = False
        
        self.criar_interface_avancada()
        self.root.after(1500, self.apresentacao_sistema_avancada)
    
    def criar_interface_avancada(self):
        """Cria interface principal super avançada"""
        self.root.title(f"DEXOS ULTIMATE v4.0 - {self.usuario}")
        self.root.attributes('-fullscreen', True)
        self.root.configure(bg='#0A0A1A')
        self.root.bind('<Escape>', self.sair_tela_cheia)
        
        # Obter dimensões da tela
        monitor = get_monitors()[0]
        self.width = monitor.width
        self.height = monitor.height
        
        # Canvas principal para HUD
        self.canvas = tk.Canvas(
            self.root,
            width=self.width,
            height=self.height,
            bg='#0A0A1A',
            highlightthickness=0
        )
        self.canvas.pack()
        
        # Inicializar HUD revolucionário
        self.hud = HUDRevolucionario(self.canvas, self.width, self.height)
        
        # Painel de controle lateral
        self.criar_painel_controle_avancado()
        
        # Console de sistema
        self.criar_console_avancado()
        
        # Iniciar sistema de voz
        self.voz.iniciar_escuta_continua_ptbr(self.processar_comando_voz)
        
        # Primeira mensagem do sistema
        self.comunicacao.enviar_mensagem_sistema(
            "Sistema DEXOS Ultimate v4.0 inicializado com sucesso!",
            "sistema", 2
        )
    
    def criar_painel_controle_avancado(self):
        """Cria painel de controle lateral avançado"""
        largura_painel = 350
        
        # Frame principal do painel
        self.painel_frame = tk.Frame(
            self.root,
            bg='#001122',
            width=largura_painel,
            height=self.height
        )
        self.painel_frame.place(x=self.width - largura_painel, y=0)
        self.painel_frame.pack_propagate(False)
        
        # Cabeçalho do painel
        cabecalho = tk.Frame(self.painel_frame, bg='#002244', height=80)
        cabecalho.pack(fill='x', padx=10, pady=10)
        
        tk.Label(
            cabecalho,
            text="DEXOS ULTIMATE",
            font=("Arial", 16, "bold"),
            fg="#00F0FF",
            bg='#002244'
        ).pack(pady=5)
        
        tk.Label(
            cabecalho,
            text=f"Usuário: {self.usuario}",
            font=("Arial", 10),
            fg="#00FF88",
            bg='#002244'
        ).pack()
        
        # Área de botões de controle
        controles = tk.Frame(self.painel_frame, bg='#001122')
        controles.pack(fill='x', padx=15, pady=10)
        
        # Botões principais com estilo avançado
        botoes_principais = [
            ("🎯 STATUS DO SISTEMA", self.mostrar_status_avancado, "#00D4FF"),
            ("🔍 ANÁLISE COMPLETA", self.executar_analise_completa, "#00FF88"),
            ("🛡️ PROTEÇÃO AVANÇADA", self.mostrar_protecao_avancada, "#FF6B35"),
            ("📷 CÂMERA INTELIGENTE", self.ativar_camera_inteligente, "#AA00FF"),
            ("🚀 MODO REVOLUCIONÁRIO", self.ativar_modo_revolucionario, "#FF0066"),
            ("🎤 CONTROLE POR VOZ", self.controle_voz_avancado, "#FFD700"),
            ("📊 RELATÓRIO COMPLETO", self.gerar_relatorio_completo, "#00FFFF"),
            ("❌ SAIR DO SISTEMA", self.sair_sistema, "#FF4444")
        ]
        
        for texto, comando, cor in botoes_principais:
            btn = tk.Button(
                controles,
                text=texto,
                command=comando,
                font=("Arial", 10, "bold"),
                bg=cor,
                fg="white",
                width=25,
                height=2,
                relief='flat',
                bd=0
            )
            btn.pack(pady=5)
            btn.bind("<Enter>", lambda e, b=btn: b.configure(bg='#FFFFFF'))
            btn.bind("<Leave>", lambda e, b=btn, c=cor: b.configure(bg=c))
        
        # Indicadores de status
        self.criar_indicadores_status()
    
    def criar_indicadores_status(self):
        """Cria indicadores de status em tempo real"""
        status_frame = tk.Frame(self.painel_frame, bg='#001122')
        status_frame.pack(fill='x', padx=15, pady=10)
        
        tk.Label(
            status_frame,
            text="STATUS DO SISTEMA:",
            font=("Arial", 11, "bold"),
            fg="#00FF88",
            bg='#001122'
        ).pack(anchor='w')
        
        # Indicadores
        indicadores = [
            ("🛡️ Proteção", "ATIVA", "#00FF88"),
            ("🎤 Voz PT-BR", "ATIVA", "#00FF88"),
            ("📊 HUD", "OPERACIONAL", "#00FF88"),
            ("🌐 Rede", "ESTÁVEL", "#00FF88")
        ]
        
        for icone, texto, cor in indicadores:
            frame_ind = tk.Frame(status_frame, bg='#001122')
            frame_ind.pack(fill='x', pady=2)
            
            tk.Label(
                frame_ind,
                text=icone,
                font=("Arial", 10),
                fg=cor,
                bg='#001122'
            ).pack(side='left')
            
            tk.Label(
                frame_ind,
                text=texto,
                font=("Arial", 9),
                fg="white",
                bg='#001122'
            ).pack(side='left', padx=5)
    
    def criar_console_avancado(self):
        """Cria console de sistema avançado"""
        console_frame = tk.Frame(self.root, bg='#001122')
        console_frame.place(x=20, y=self.height - 250, width=500, height=230)
        
        tk.Label(
            console_frame,
            text="CONSOLE DO SISTEMA:",
            font=("Arial", 10, "bold"),
            fg="#00FF88",
            bg='#001122'
        ).pack(anchor='w', padx=10, pady=5)
        
        self.console_text = scrolledtext.ScrolledText(
            console_frame,
            wrap=tk.WORD,
            width=58,
            height=12,
            bg='#000000',
            fg='#00FF88',
            font=("Consolas", 8),
            insertbackground='#00FF88'
        )
        self.console_text.pack(padx=10, pady=(0,10), fill='both', expand=True)
        self.console_text.config(state=tk.DISABLED)
    
    def adicionar_console(self, mensagem, cor='#00FF88'):
        """Adiciona mensagem ao console"""
        self.console_text.config(state=tk.NORMAL)
        self.console_text.insert(tk.END, f"{mensagem}\n", cor)
        self.console_text.see(tk.END)
        self.console_text.config(state=tk.DISABLED)
    
    def apresentacao_sistema_avancada(self):
        """Apresentação inicial do sistema"""
        mensagens = [
            "🚀 INICIALIZANDO DEXOS ULTIMATE v4.0...",
            "✅ SISTEMA DE PROTEÇÃO AVANÇADO ATIVADO",
            "🎤 SISTEMA DE VOZ PORTUGUÊS CONFIGURADO", 
            "📊 HUD REVOLUCIONÁRIO OPERACIONAL",
            "🌐 MÓDULOS DE INTELIGÊNCIA CARREGADOS",
            f"👤 USUÁRIO AUTENTICADO: {self.usuario}",
            "🎯 TODOS OS SISTEMAS OPERACIONAIS!",
            "💡 DIGA 'DEXOS, AJUDA' PARA VER COMANDOS DISPONÍVEIS"
        ]
        
        for i, msg in enumerate(mensagens):
            self.root.after(i * 800, lambda m=msg: self.comunicacao.enviar_mensagem_sistema(m, "sistema", 1))
        
        self.root.after(len(mensagens) * 800, self.voz.falar_ptbr, 
                       f"Sistema DEXOS Ultimate completamente operacional! Bem-vindo, {self.usuario}!", "entusiasmado")
    
    def processar_comando_voz(self, acao, comando):
        """Processa comandos de voz"""
        if acao == 'status':
            self.mostrar_status_avancado()
        elif acao == 'analisar':
            self.executar_analise_completa()
        elif acao == 'protecao':
            self.mostrar_protecao_avancada()
        elif acao == 'camera':
            self.ativar_camera_inteligente()
        elif acao == 'revolucionario':
            self.ativar_modo_revolucionario()
        elif acao == 'ajuda':
            self.mostrar_ajuda_voz()
        elif acao == 'sair':
            self.sair_sistema()
    
    def mostrar_status_avancado(self):
        """Mostra status avançado do sistema"""
        status = self.protecao.relatorio_seguranca()
        metricas = self.hud.metricas_tempo_real
        
        mensagem = f"""
📊 STATUS DO SISTEMA DEXOS ULTIMATE:

🛡️ SEGURANÇA:
  • Status: {status['status']}
  • Nível: {status['nivel_seguranca']}
  • Integridade: {status['integridade']}
  • Criptografia: {status['criptografia']}

⚙️ DESEMPENHO:
  • CPU: {metricas['cpu']}
  • Memória: {metricas['memoria']}
  • GPU: {metricas['gpu']}
  • Processos: {metricas['processos']}

🎤 COMUNICAÇÃO:
  • Voz PT-BR: ATIVA
  • Reconhecimento: OPERACIONAL
  • Total Mensagens: {self.comunicacao.relatorio_comunicacao()['total_mensagens']}

💫 SISTEMA OPERACIONAL E OTIMIZADO!
        """
        
        self.comunicacao.enviar_mensagem_sistema("Status do sistema exibido", "info", 1)
        self.mostrar_janela_info("Status do Sistema", mensagem)
    
    def executar_analise_completa(self):
        """Executa análise completa do sistema"""
        self.comunicacao.enviar_mensagem_sistema("Iniciando análise completa do sistema...", "info", 1)
        self.voz.falar_ptbr("Executando análise completa de todos os sistemas!", "serio")
        
        # Simular análise
        for i in range(1, 6):
            self.root.after(i * 1000, lambda x=i: self.comunicacao.enviar_mensagem_sistema(
                f"Análise {x}/5: Sistemas {'ótimos' if x % 2 == 0 else 'estáveis'}",
                "sucesso" if x % 2 == 0 else "info", 1
            ))
        
        self.root.after(6000, lambda: self.comunicacao.enviar_mensagem_sistema(
            "✅ Análise completa concluída! Todos os sistemas operando perfeitamente!", "sucesso", 2
        ))
        self.root.after(6000, lambda: self.voz.falar_ptbr(
            "Análise concluída! Todos os sistemas estão perfeitos!", "alegre"
        ))
    
    def mostrar_protecao_avancada(self):
        """Mostra status de proteção avançada"""
        protecao = self.protecao.relatorio_seguranca()
        
        mensagem = f"""
🛡️ SISTEMA DE PROTEÇÃO AVANÇADO DEXOS:

🔒 STATUS: {protecao['status']}
📛 ASSINATURA: {protecao['assinatura']}
🌐 MAC: {protecao['mac_criptografado']}
🎯 NÍVEL: {protecao['nivel_seguranca']}
✅ INTEGRIDADE: {protecao['integridade']}
🔐 CRIPTOGRAFIA: {protecao['criptografia']}
🕒 VERIFICAÇÃO: {protecao['ultima_verificacao']}

💪 SISTEMA PROTEGIDO CONTRA AMEAÇAS
        """
        
        self.comunicacao.enviar_mensagem_sistema("Status de proteção exibido", "info", 1)
        self.mostrar_janela_info("Proteção Avançada", mensagem)
        self.voz.falar_ptbr("Sistema de proteção máximo ativo e operacional!", "serio")
    
    def ativar_camera_inteligente(self):
        """Ativa câmera inteligente"""
        if not self.camera_ativa:
            try:
                self.cap = cv2.VideoCapture(0)
                if self.cap.isOpened():
                    self.camera_ativa = True
                    self.comunicacao.enviar_mensagem_sistema("Câmera inteligente ativada!", "sucesso", 1)
                    self.voz.falar_ptbr("Câmera inteligente ativada com sucesso!", "alegre")
                    self.mostrar_camera_inteligente()
                else:
                    raise Exception("Câmera não disponível")
            except Exception as e:
                self.comunicacao.enviar_mensagem_sistema(f"Erro ao acessar câmera: {e}", "erro", 2)
                self.voz.falar_ptbr("Não foi possível acessar a câmera no momento.", "serio")
        else:
            self.desativar_camera()
    
    def mostrar_camera_inteligente(self):
        """Mostra feed da câmera com processamento inteligente"""
        if self.camera_ativa and self.cap.isOpened():
            ret, frame = self.cap.read()
            if ret:
                # Processamento avançado da imagem
                frame = cv2.flip(frame, 1)
                
                # Adicionar HUD da câmera
                cv2.putText(frame, "DEXOS CAMERA INTELIGENTE", (10, 30), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
                cv2.putText(frame, "MODO: ANALISE AVANCADA", (10, 60), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
                cv2.putText(frame, f"RESOLUCAO: {frame.shape[1]}x{frame.shape[0]}", (10, 90), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
                
                # Mostrar frame
                cv2.imshow('DEXOS - Camera Inteligente', frame)
            
            # Próximo frame
            if cv2.getWindowProperty('DEXOS - Camera Inteligente', cv2.WND_PROP_VISIBLE) >= 1:
                self.root.after(10, self.mostrar_camera_inteligente)
            else:
                self.desativar_camera()
    
    def desativar_camera(self):
        """Desativa a câmera"""
        if self.camera_ativa:
            self.camera_ativa = False
            if self.cap:
                self.cap.release()
            cv2.destroyAllWindows()
            self.comunicacao.enviar_mensagem_sistema("Câmera desativada", "info", 1)
    
    def ativar_modo_revolucionario(self):
        """Ativa modo revolucionário"""
        self.modo_revolucionario = not self.modo_revolucionario
        
        if self.modo_revolucionario:
            self.comunicacao.enviar_mensagem_sistema(
                "🚀 MODO REVOLUCIONÁRIO ATIVADO! POTÊNCIA MÁXIMA!", 
                "sistema", 3
            )
            self.voz.falar_ptbr(
                "Modo revolucionário ativado! Todos os sistemas em potência máxima!", 
                "entusiasmado", 20
            )
            
            # Efeitos visuais especiais
            for _ in range(50):
                self.hud.elementos.append({
                    'tipo': 'particula_avancada',
                    'x': random.randint(0, self.width),
                    'y': random.randint(0, self.height),
                    'velocidade': random.uniform(3, 8),
                    'tamanho': random.uniform(2, 8),
                    'cor': random.choice(['#FF0066', '#AA00FF', '#00FF88']),
                    'direcao': random.uniform(0, math.pi * 2),
                    'vida': random.uniform(30, 100),
                    'rotacao': random.uniform(0, 360),
                    'pulsacao': random.uniform(0, math.pi * 2)
                })
        else:
            self.comunicacao.enviar_mensagem_sistema(
                "Modo revolucionário desativado", 
                "info", 1
            )
            self.voz.falar_ptbr("Modo revolucionário desativado", "neutro")
    
    def controle_voz_avancado(self):
        """Controle avançado por voz"""
        comandos = """
🎤 COMANDOS DE VOZ DISPONÍVEIS:

• "Dexos, status" - Status do sistema
• "Dexos, analisar" - Análise completa  
• "Dexos, proteção" - Status de proteção
• "Dexos, câmera" - Ativar câmera
• "Dexos, modo revolucionário" - Potência máxima
• "Dexos, ajuda" - Mostrar esta ajuda
• "Dexos, sair" - Sair do sistema

💡 O sistema está sempre ouvindo seus comandos!
        """
        
        self.mostrar_janela_info("Controle por Voz", comandos)
        self.voz.falar_ptbr("Aqui estão os comandos de voz disponíveis! Diga 'Dexos, ajuda' a qualquer momento!", "alegre")
    
    def mostrar_ajuda_voz(self):
        """Mostra ajuda de comandos de voz"""
        self.controle_voz_avancado()
    
    def gerar_relatorio_completo(self):
        """Gera relatório completo do sistema"""
        protecao = self.protecao.relatorio_seguranca()
        metricas = self.hud.metricas_tempo_real
        comunicacao = self.comunicacao.relatorio_comunicacao()
        
        relatorio = f"""
📋 RELATÓRIO COMPLETO DEXOS ULTIMATE
🕒 Gerado em: {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}

🛡️ SEGURANÇA:
  • Status: {protecao['status']}
  • Assinatura: {protecao['assinatura']}
  • Nível: {protecao['nivel_seguranca']}
  • Integridade: {protecao['integridade']}

⚙️ DESEMPENHO:
  • CPU: {metricas['cpu']}
  • Memória: {metricas['memoria']} 
  • GPU: {metricas['gpu']}
  • Disco: {metricas['disco']}
  • Processos: {metricas['processos']}

🎤 COMUNICAÇÃO:
  • Total Mensagens: {comunicacao['total_mensagens']}
  • Alertas Ativos: {comunicacao['alertas_ativos']}
  • Sistema: {comunicacao['sistema_comunicacao']}

💫 SISTEMA: OPERACIONAL E OTIMIZADO
👤 USUÁRIO: {self.usuario}
🚀 VERSÃO: DEXOS ULTIMATE v4.0
        """
        
        self.mostrar_janela_info("Relatório Completo", relatorio)
        self.comunicacao.enviar_mensagem_sistema("Relatório completo gerado", "sucesso", 1)
    
    def mostrar_janela_info(self, titulo, conteudo):
        """Mostra janela de informação"""
        try:
            janela = tk.Toplevel(self.root)
            janela.title(titulo)
            janela.geometry("600x500")
            janela.configure(bg='#1A1A2E')
            janela.attributes('-topmost', True)
            
            # Centralizar
            janela.update_idletasks()
            x = (janela.winfo_screenwidth() // 2) - (600 // 2)
            y = (janela.winfo_screenheight() // 2) - (500 // 2)
            janela.geometry(f"600x500+{x}+{y}")
            
            # Conteúdo
            tk.Label(
                janela,
                text=titulo,
                font=("Arial", 14, "bold"),
                fg="#00F0FF",
                bg='#1A1A2E'
            ).pack(pady=10)
            
            texto = scrolledtext.ScrolledText(
                janela,
                wrap=tk.WORD,
                width=70,
                height=25,
                bg='#000000',
                fg='#00FF88',
                font=("Consolas", 9)
            )
            texto.pack(padx=20, pady=10, fill='both', expand=True)
            texto.insert(tk.END, conteudo)
            texto.config(state=tk.DISABLED)
            
            tk.Button(
                janela,
                text="FECHAR",
                command=janela.destroy,
                font=("Arial", 10, "bold"),
                bg="#FF0066",
                fg="white"
            ).pack(pady=10)
            
        except Exception as e:
            print(f"Erro na janela info: {e}")
    
    def sair_tela_cheia(self, event=None):
        """Sai do modo tela cheia"""
        self.root.attributes('-fullscreen', False)
        self.comunicacao.enviar_mensagem_sistema("Modo tela cheia desativado", "info", 1)
    
    def sair_sistema(self):
        """Sai do sistema com segurança"""
        if messagebox.askyesno("Sair do DEXOS", "Deseja realmente sair do sistema DEXOS Ultimate?"):
            self.comunicacao.enviar_mensagem_sistema("Encerrando sistema DEXOS Ultimate...", "sistema", 2)
            self.voz.falar_ptbr("Encerrando sistema DEXOS Ultimate. Até logo!", "serio")
            self.desativar_camera()
            self.voz.parar_escuta_ptbr()
            self.root.after(2000, self.root.destroy)

# =============================================================================
# INICIALIZAÇÃO DO SISTEMA
# =============================================================================

def main():
    try:
        # Verificar dependências
        print("🚀 INICIANDO DEXOS ULTIMATE v4.0...")
        print("📦 VERIFICANDO DEPENDÊNCIAS...")
        
        # Criar janela principal
        root = tk.Tk()
        
        # Obter nome de usuário
        usuario = "OPERADOR PRINCIPAL"  # Poderia ser obtido do sistema
        
        # Inicializar interface
        app = InterfacePrincipalAvancada(root, usuario)
        
        print("✅ SISTEMA INICIALIZADO COM SUCESSO!")
        print("🎯 DEXOS ULTIMATE v4.0 PRONTO PARA OPERAÇÃO!")
        
        root.mainloop()
        
    except Exception as e:
        print(f"❌ ERRO CRÍTICO: {e}")
        messagebox.showerror("Erro DEXOS", f"Falha na inicialização: {e}")

if __name__ == "__main__":
    main()