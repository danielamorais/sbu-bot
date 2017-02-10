#/bin/bash
PYTHON="/usr/bin/python"
BOT_PATH="/usr/local/bin/sbu-bot"
VENV_PATH="/usr/local/bin/sbu-bot/venv/bin"
CONFIG_DIR="$HOME/.sbu-bot"
CONFIG_FILE="$CONFIG_DIR/config.yml"

echo "Criando arquivo de configuração..."
echo -n "Entre seu email: "
read EMAIL
echo -n "Entre sua senha: "
read SENHA
rm -rf $CONFIG_DIR
mkdir $CONFIG_DIR
echo "email: $EMAIL" >> $CONFIG_FILE
echo "senha: $SENHA" >> $CONFIG_FILE
echo "Arquivo de configuração salvo em $CONFIG_FILE"

echo "Instalando script..."
sudo rm -rf $BOT_PATH

echo "Copiando arquivos para $BOT_PATH"
sudo mkdir $BOT_PATH
sudo cp -r * $BOT_PATH
sudo chmod +x "$BOT_PATH/download_gecko.sh"
sudo chmod 755 "$BOT_PATH/bot.py"

echo "Configurando virtualenv..."
sudo virtualenv -p $PYTHON "$BOT_PATH/venv"
sudo -E "$VENV_PATH/python" -m pip install -U pip
sudo -E "$VENV_PATH/pip" install -r requirements.txt
echo "Baixando e instalando geckodriver..."
sudo bash "$BOT_PATH/download_gecko.sh"
sudo chmod 755 "$BOT_PATH/geckodriver"

echo "Instalando cronjob..."
COMANDO="$VENV_PATH/python $BOT_PATH/bot.py > /dev/null"
JOB="0 */3 * * * $COMANDO"
cat <(fgrep -i -v "$COMANDO" <(crontab -l)) <(echo "$JOB") | crontab -
# adapted from Stoutie answer on stack overflow:
# https://stackoverflow.com/questions/878600/how-to-create-cronjob-using-bash
echo "Pronto."
