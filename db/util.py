from snowflake import SnowflakeGenerator
import os

sf = SnowflakeGenerator(int(os.environ["NODE_ID"]))
