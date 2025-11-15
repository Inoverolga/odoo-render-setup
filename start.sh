#!/bin/bash

# Ждем базу данных
until pg_isready -h $HOST -p $PORT -U $USER; do
  echo "Waiting for database..."
  sleep 2
done

# Пытаемся инициализировать базу (игнорируем ошибки python-ldap)
python3 /usr/bin/odoo -d $DATABASE -i base --without-demo=all --stop-after-init || true

# Запускаем Odoo (игнорируем предупреждения)
exec python3 /usr/bin/odoo