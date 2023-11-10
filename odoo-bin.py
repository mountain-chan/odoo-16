# python3 odoo-bin.py -c conf/odoo.conf

# set server timezone in UTC before time module imported
__import__('os').environ['TZ'] = 'UTC'
import odoo

if __name__ == "__main__":
    odoo.cli.main()
