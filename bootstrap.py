#-*- coding: UTF-8 -*-
from Configuration.config import Config
import logging
from logger.boot import setupLogging
from Controller.FtpLoader import FtpLoader
from Model.geoCsv import *
import zipfile

if __name__ == '__main__' :

    setupLogging()
    logger = logging.getLogger(__name__)

    config = Config()
    urls = config.get_property("URL")
    for domain in urls :
        for dom, url in domain.items() :
            ftp = FtpLoader(url)
            download_dir = config.get_property("WS").get("DOWNLOAD").get(dom)
            for file in config.get_property("FILES").get(dom) :
                ftp.downloadFileItem(file, outDir=download_dir)
                with zipfile.ZipFile(os.path.join(download_dir, file), 'r') as zip_ref:
                    zip_ref.extractall(download_dir)
                checkPointsFromFile(download_dir, file[:-3])


