import os
import django

# 手动启动 Django
# 配置环境变量
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'weather_analysis.settings')

# 启动 Django
django.setup()
