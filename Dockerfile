FROM odoo:16

# Устанавливаем системные зависимости для python-ldap
USER root
RUN apt-get update && apt-get install -y \
    postgresql-client \
    libsasl2-dev \
    libldap2-dev \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем Python зависимости
RUN pip3 install python-ldap

USER odoo