from flask import Flask, render_template, jsonify, request
from src.helper import download_hugging_face_embeddings