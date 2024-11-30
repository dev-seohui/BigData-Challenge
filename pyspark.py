# 설치
!pip install pyspark

# 패키지 불러오기
import pyspark

# sql 모듈
from pyspark.sql
from pyspark.sql import Row
from pyspark.sql import SparkSession
from pyspark.sql import functions

# sql > functions 모듈
from pyspark.sql.functions import col
from pyspark.sql.functions import types
from pyspark.sql.functions import asc
from pyspark.sql.functions import desc
from pyspark.sql.functions import avg
from pyspark.sql.functions import round as rnd # 파이썬의 내장함수와 겹치므로 별칭 지정
