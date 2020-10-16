from source.config import logger
from flask import Flask,request,jsonify
from flask_restful import Resource, Api

def isAlive():
    logger.log_text('Inside isAlive method', severity='INFO')
    print("Inside isAlive method")
    return '{"msg":"i am alive"}', 200