from flask import Flask
import logging
import os
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)

# Настраиваем логирование
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Настраиваем метрики для Prometheus
metrics = PrometheusMetrics(app)
# Теперь /metrics будет доступен по адресу http://localhost:5000/metrics


@app.route('/')
def home():
    logger.info("Главная страница запрошена")
    return "<h1>Привет от Flask-приложения!</h1><p>Всё работает 👍</p>"


@app.route('/crash')
def crash():
    logger.error("Вызван сбой!")
    raise Exception("Искусственная ошибка для тестирования!")


@app.route('/health')
def health():
    return {"status": "OK"}, 200


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
