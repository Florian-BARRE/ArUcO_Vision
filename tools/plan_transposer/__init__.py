from configuration import APP_CONFIG

from tools.plan_transposer.object import PlanTransposer

plan_transposer = PlanTransposer(
    camera_table_distance=APP_CONFIG.CAMERA_TABLE_DISTANCE,
    alpha=APP_CONFIG.CAMERA_OBJECT_FUNCTION_A,
    beta=APP_CONFIG.CAMERA_OBJECT_FUNCTION_B
)
