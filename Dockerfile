FROM python:3.8
RUN pip install odoo==16.0
EXPOSE 8069
CMD ["odoo"]