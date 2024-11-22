# RedisPlay CLI

RedisPlay é uma ferramenta de linha de comando (CLI) que permite ajustar facilmente a temperatura da cor do seu monitor usando o comando `xrandr`. Com o RedisPlay, você pode alterar rapidamente a temperatura da cor para quente, frio ou normal, proporcionando uma experiência visual mais confortável e personalizada.

## Recursos

- Ajuste rápido da temperatura da cor do monitor
- Suporte para múltiplos monitores
- Interface de linha de comando simples e intuitiva
- Configuração fácil e rápida

## Instalação

1. Clone este repositório para o seu sistema local:
   ```
   git clone https://github.com/jonbrand/redisplay.git
   ```

2. Navegue até o diretório do projeto:
   ```
   cd redisplay
   ```

3. Dê permissão de execução ao arquivo `redisplay`:
   ```
   chmod +x redisplay
   ```

4. Adicione o diretório do projeto ao seu PATH. Abra o arquivo `~/.bashrc` (para Bash) ou `~/.zshrc` (para Zsh) em um editor de texto e adicione a seguinte linha ao final do arquivo:
   ```
   export PATH="/caminho/para/redisplay:$PATH"
   ```
   Substitua `/caminho/para/redisplay` pelo caminho completo do diretório do projeto.

5. Feche e reabra o terminal ou execute o seguinte comando para aplicar as alterações:
   ```
   source ~/.bashrc
   ```
   ou
   ```
   source ~/.zshrc
   ```

## Uso

Para usar o RedisPlay, abra o terminal e execute o comando `redisplay` seguido do comando desejado:

- Para definir a temperatura da cor como quente:
  ```
  redisplay warm
  ```

- Para definir a temperatura da cor como fria:
  ```
  redisplay cool
  ```

- Para definir a temperatura da cor como normal:
  ```
  redisplay normal
  ```

Se você tiver vários monitores conectados, o RedisPlay solicitará que você selecione o monitor desejado.

Você também pode especificar o monitor usando a opção `--monitor` ou `-m`:
```
redisplay warm --monitor HDMI-1
```

## Contribuição

Contribuições são bem-vindas! Se você encontrar algum problema, tiver sugestões ou quiser adicionar novos recursos, fique à vontade para abrir uma issue ou enviar um pull request.

Ao contribuir, por favor, siga as diretrizes de contribuição do projeto e certifique-se de que o seu código esteja de acordo com o estilo e as convenções utilizadas.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

## Inspiração do Projeto

O RedisPlay foi inspirado na necessidade de uma maneira fácil e rápida de ajustar a temperatura da cor do monitor para melhorar o conforto visual e reduzir a fadiga ocular e também serviu como uma forma de estudar a linguagem de programação Python.