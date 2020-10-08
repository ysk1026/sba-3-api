import tensorflow as tf
import tensorflow_hub as hub
def env_info():
    print(f'TF 버전 : {tf.__version__}')
    print(f'즉시 실행 모드 : {tf.executing_eagerly()}')
    print(f'허브버전 : {hub.__version__}')
    print("GPU ", "사용 가능" if tf.config.experimental.list_physical_devices("GPU") else "사용 불가능")
    