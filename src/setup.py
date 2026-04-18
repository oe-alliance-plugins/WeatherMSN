from setuptools import setup
import setup_translate

pkg = 'Extensions.WeatherMSN'
setup(name='enigma2-plugin-extensions-weathermsn',
       version='1.0',
       description='WeatherMSN',
       package_dir={pkg: 'WeatherMSN'},
       packages=[pkg],
       package_data={pkg: ['icons/moon/*.png', 'icons/weather/*.png', 'buttons/*.png', '*.png', '*.xml', 'locale/*/LC_MESSAGES/*.mo']},
       cmdclass=setup_translate.cmdclass,  # for translation
      )
