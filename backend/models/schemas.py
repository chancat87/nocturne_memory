from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any


class DiffRequest(BaseModel):
    text_a: str = Field(..., description="旧文本")
    text_b: str = Field(..., description="新文本")


class DiffResponse(BaseModel):
    diff_html: str = Field(..., description="HTML格式的diff")
    diff_unified: str = Field(..., description="unified格式的diff")
    summary: str = Field(..., description="变化摘要")


# ============ Review / Rollback ============

class ChangeInfo(BaseModel):
    """One affected URI in the changeset pool."""
    uri: str
    change_type: str  # "created", "modified", "deleted"


class UriDiff(BaseModel):
    """Diff between before-state and current DB state for one URI."""
    uri: str
    change_type: str
    before_content: Optional[str] = None
    current_content: Optional[str] = None
    before_meta: Optional[Dict[str, Any]] = None
    current_meta: Optional[Dict[str, Any]] = None
    has_changes: bool


class RollbackResponse(BaseModel):
    uri: str
    success: bool
    message: str


class ChangeGroup(BaseModel):
    node_uuid: str
    display_uri: str
    top_level_table: str
    row_count: int


class GroupRollbackResponse(BaseModel):
    node_uuid: str
    success: bool
    message: str

