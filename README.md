# sbu-bot
Bot para renovar os livros emprestados da biblioteca.

## Instalação
A instalação é simples.

* Primeiramente clone este repositório num diretório de sua preferência
    ```bash
    $ git clone https://github.com/prcaetano/sbu-bot.git
    ```

* Certifique-se que possui virtualenv instalado em seu sistema. Em sistemas debian-like você pode instalá-lo com os comandos
    ```bash
    $ sudo apt update
    $ sudo apt install virtualenv
    ```

* Execute o script `install.sh`
    ```bash
    $ bash install.sh
    ```

O script pedirá seu email e senha do acervus. Ele instalará o robô no diretório `/usr/local/bin/sbu-bot`.
Um arquivo de configuração contendo as linhas
    ```yml
    email: leitor_avido_e_esquecido@dac.unicamp.br
    senha: 5up3r53gr3d0
    ```
será salvo em `$HOME/.sbu-bot/config.yml`. A linha `0 */3 * * * /usr/local/bin/sbu-bot/venv/bin/python /usr/local/bin/sbu-bot/bot.py > /dev/null` será adicionada ao crontab de seu usuário e o robô tentará a cada 3 horas todos os dias renovar seus livros (entretanto, após ter sido rodado com sucesso ele não tentará renovar novamente até o dia seguinte). O log do robô fica no arquivo `$HOME/.sbu-bot/log.log`.

## Desinstalação

* Remova as pastas contendo o script e as configurações
    ```bash
    $ sudo rm -rf /usr/local/bin/sbu-bot
    $ rm -rf ~/.sbu-bot
    ```

* Delete o cron job, executando
    ```bash
    $ crontab -e
    ```
e removendo a linha `0 */3 * * * /usr/local/bin/sbu-bot/venv/bin/python /usr/local/bin/sbu-bot/bot.py > /dev/null`.

## Garantias
Este robô não foi amplamente testado e não deve ser responsabilizado por desesperos às vésperas da P3.
