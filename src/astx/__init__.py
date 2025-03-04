# mypy: disable-error-code="attr-defined"
"""ASTx."""

from importlib import metadata as importlib_metadata

from astx import (
    base,
    blocks,
    callables,
    flows,
    literals,
    mixes,
    packages,
    symbol_table,
    types,
    variables,
)
from astx.base import (
    AST,
    ASTKind,
    ASTNodes,
    DataType,
    Expr,
    ExprType,
    Identifier,
    OperatorType,
    SourceLocation,
    StatementType,
    Undefined,
)
from astx.blocks import (
    Block,
)
from astx.callables import (
    Argument,
    Arguments,
    Function,
    FunctionCall,
    FunctionPrototype,
    FunctionReturn,
    LambdaExpr,
)
from astx.classes import (
    ClassDeclStmt,
    ClassDefStmt,
    EnumDeclStmt,
    StructDeclStmt,
    StructDefStmt,
)
from astx.exceptions import (
    CatchHandlerStmt,
    ExceptionHandlerStmt,
    FinallyHandlerStmt,
    ThrowStmt,
)
from astx.flows import (
    CaseStmt,
    ForCountLoopExpr,
    ForCountLoopStmt,
    ForRangeLoopExpr,
    ForRangeLoopStmt,
    GotoStmt,
    IfExpr,
    IfStmt,
    SwitchStmt,
    WhileExpr,
    WhileStmt,
    YieldExpr,
)
from astx.literals import (
    Literal,
    LiteralBoolean,
    LiteralComplex,
    LiteralComplex32,
    LiteralComplex64,
    LiteralDate,
    LiteralDateTime,
    LiteralFloat16,
    LiteralFloat32,
    LiteralFloat64,
    LiteralInt8,
    LiteralInt16,
    LiteralInt32,
    LiteralInt64,
    LiteralInt128,
    LiteralNone,
    LiteralString,
    LiteralTime,
    LiteralTimestamp,
    LiteralUInt8,
    LiteralUInt16,
    LiteralUInt32,
    LiteralUInt64,
    LiteralUInt128,
    LiteralUTF8Char,
    LiteralUTF8String,
)
from astx.mixes import (
    NamedExpr,
)
from astx.modifiers import (
    MutabilityKind,
    ScopeKind,
    VisibilityKind,
)
from astx.operators import AssignmentExpr, VariableAssignment, WalrusOp
from astx.packages import (
    AliasExpr,
    ImportExpr,
    ImportFromExpr,
    ImportFromStmt,
    ImportStmt,
    Module,
    Package,
    Program,
    Target,
)
from astx.subscript import SubscriptExpr
from astx.types import (
    BinaryOp,
    Boolean,
    Complex,
    Complex32,
    Complex64,
    DataTypeOps,
    Date,
    DateTime,
    Float16,
    Float32,
    Float64,
    Floating,
    Int8,
    Int16,
    Int32,
    Int64,
    Integer,
    Number,
    SignedInteger,
    String,
    Time,
    Timestamp,
    TypeCastExpr,
    UInt8,
    UInt16,
    UInt32,
    UInt64,
    UInt128,
    UnaryOp,
    UnsignedInteger,
    UTF8Char,
    UTF8String,
)
from astx.variables import (
    InlineVariableDeclaration,
    Variable,
    VariableDeclaration,
)


def get_version() -> str:
    """Return the program version."""
    try:
        return importlib_metadata.version(__name__)
    except importlib_metadata.PackageNotFoundError:  # pragma: no cover
        return "0.17.0"  # semantic-release


__all__ = [
    "AST",
    "ASTKind",
    "ASTNodes",
    "AliasExpr",
    "Argument",
    "Arguments",
    "AssignmentExpr",
    "BinaryOp",
    "Block",
    "Boolean",
    "CaseStmt",
    "CatchHandlerStmt",
    "ClassDeclStmt",
    "ClassDefStmt",
    "Complex",
    "Complex32",
    "Complex64",
    "DataType",
    "DataTypeOps",
    "Date",
    "DateTime",
    "EnumDeclStmt",
    "ExceptionHandlerStmt",
    "Expr",
    "ExprType",
    "FinallyHandlerStmt",
    "Float16",
    "Float32",
    "Float64",
    "Floating",
    "ForCountLoopExpr",
    "ForCountLoopStmt",
    "ForRangeLoopExpr",
    "ForRangeLoopStmt",
    "Function",
    "FunctionCall",
    "FunctionPrototype",
    "FunctionReturn",
    "GotoStmt",
    "Identifier",
    "IfExpr",
    "IfStmt",
    "ImportExpr",
    "ImportFromExpr",
    "ImportFromStmt",
    "ImportStmt",
    "InlineVariableDeclaration",
    "Int8",
    "Int16",
    "Int32",
    "Int64",
    "Integer",
    "LambdaExpr",
    "Literal",
    "LiteralBoolean",
    "LiteralComplex",
    "LiteralComplex32",
    "LiteralComplex64",
    "LiteralDate",
    "LiteralDateTime",
    "LiteralFloat16",
    "LiteralFloat32",
    "LiteralFloat64",
    "LiteralInt8",
    "LiteralInt16",
    "LiteralInt32",
    "LiteralInt64",
    "LiteralInt128",
    "LiteralNone",
    "LiteralString",
    "LiteralTime",
    "LiteralTimestamp",
    "LiteralUInt8",
    "LiteralUInt16",
    "LiteralUInt32",
    "LiteralUInt64",
    "LiteralUInt128",
    "LiteralUTF8Char",
    "LiteralUTF8String",
    "Module",
    "MutabilityKind",
    "NamedExpr",
    "Number",
    "OperatorType",
    "Package",
    "Program",
    "ScopeKind",
    "SignedInteger",
    "SourceLocation",
    "StatementType",
    "String",
    "StructDeclStmt",
    "StructDefStmt",
    "SubscriptExpr",
    "SwitchStmt",
    "Target",
    "ThrowStmt",
    "Time",
    "Timestamp",
    "TypeCastExpr",
    "UInt8",
    "UInt16",
    "UInt32",
    "UInt64",
    "UInt128",
    "UTF8Char",
    "UTF8String",
    "UnaryOp",
    "Undefined",
    "UnsignedInteger",
    "Variable",
    "VariableAssignment",
    "VariableDeclaration",
    "VisibilityKind",
    "WalrusOp",
    "WhileExpr",
    "WhileStmt",
    "YieldExpr",
    "base",
    "blocks",
    "callables",
    "datatypes",
    "flows",
    "get_version",
    "literals",
    "mixes",
    "packages",
    "symbol_table",
    "types",
    "variables",
]


version: str = get_version()

__author__ = "Ivan Ogasawara"
__email__ = "ivan.ogasawara@gmail.com"
__version__: str = version
