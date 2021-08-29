/* A Bison parser, made by GNU Bison 2.7.  */

/* Bison interface for Yacc-like parsers in C
   
      Copyright (C) 1984, 1989-1990, 2000-2012 Free Software Foundation, Inc.
   
   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.
   
   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.
   
   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.
   
   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */

#ifndef YY_EGGYY_BUILT_X64_TMP_PARSER_YXX_H_INCLUDED
# define YY_EGGYY_BUILT_X64_TMP_PARSER_YXX_H_INCLUDED
/* Enabling traces.  */
#ifndef YYDEBUG
# define YYDEBUG 0
#endif
#if YYDEBUG
extern int eggyydebug;
#endif

/* Tokens.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
   /* Put the tokens into the symbol table, so that GDB and other debuggers
      know about them.  */
   enum yytokentype {
     EGG_NUMBER = 258,
     EGG_ULONG = 259,
     EGG_STRING = 260,
     ANIMPRELOAD = 261,
     BEZIERCURVE = 262,
     BFACE = 263,
     BILLBOARD = 264,
     BILLBOARDCENTER = 265,
     BINORMAL = 266,
     BUNDLE = 267,
     CLOSED = 268,
     COLLIDE = 269,
     COMMENT = 270,
     COMPONENT = 271,
     COORDSYSTEM = 272,
     CV = 273,
     DART = 274,
     DNORMAL = 275,
     DRGBA = 276,
     DUV = 277,
     DXYZ = 278,
     DCS = 279,
     DISTANCE = 280,
     DTREF = 281,
     DYNAMICVERTEXPOOL = 282,
     EXTERNAL_FILE = 283,
     GROUP = 284,
     DEFAULTPOSE = 285,
     JOINT = 286,
     KNOTS = 287,
     INCLUDE = 288,
     INSTANCE = 289,
     LINE = 290,
     LOOP = 291,
     MATERIAL = 292,
     MATRIX3 = 293,
     MATRIX4 = 294,
     MODEL = 295,
     MREF = 296,
     NORMAL = 297,
     NURBSCURVE = 298,
     NURBSSURFACE = 299,
     OBJECTTYPE = 300,
     ORDER = 301,
     OUTTANGENT = 302,
     PATCH = 303,
     POINTLIGHT = 304,
     POLYGON = 305,
     REF = 306,
     RGBA = 307,
     ROTATE = 308,
     ROTX = 309,
     ROTY = 310,
     ROTZ = 311,
     SANIM = 312,
     SCALAR = 313,
     SCALE = 314,
     SEQUENCE = 315,
     SHADING = 316,
     SWITCH = 317,
     SWITCHCONDITION = 318,
     TABLE = 319,
     TABLE_V = 320,
     TAG = 321,
     TANGENT = 322,
     TEXLIST = 323,
     TEXTURE = 324,
     TLENGTHS = 325,
     TRANSFORM = 326,
     TRANSLATE = 327,
     TREF = 328,
     TRIANGLEFAN = 329,
     TRIANGLESTRIP = 330,
     TRIM = 331,
     TXT = 332,
     UKNOTS = 333,
     UV = 334,
     AUX = 335,
     VKNOTS = 336,
     VERTEX = 337,
     VERTEXANIM = 338,
     VERTEXPOOL = 339,
     VERTEXREF = 340,
     XFMANIM = 341,
     XFMSANIM = 342,
     START_EGG = 343,
     START_GROUP_BODY = 344,
     START_TEXTURE_BODY = 345,
     START_PRIMITIVE_BODY = 346
   };
#endif
/* Tokens.  */
#define EGG_NUMBER 258
#define EGG_ULONG 259
#define EGG_STRING 260
#define ANIMPRELOAD 261
#define BEZIERCURVE 262
#define BFACE 263
#define BILLBOARD 264
#define BILLBOARDCENTER 265
#define BINORMAL 266
#define BUNDLE 267
#define CLOSED 268
#define COLLIDE 269
#define COMMENT 270
#define COMPONENT 271
#define COORDSYSTEM 272
#define CV 273
#define DART 274
#define DNORMAL 275
#define DRGBA 276
#define DUV 277
#define DXYZ 278
#define DCS 279
#define DISTANCE 280
#define DTREF 281
#define DYNAMICVERTEXPOOL 282
#define EXTERNAL_FILE 283
#define GROUP 284
#define DEFAULTPOSE 285
#define JOINT 286
#define KNOTS 287
#define INCLUDE 288
#define INSTANCE 289
#define LINE 290
#define LOOP 291
#define MATERIAL 292
#define MATRIX3 293
#define MATRIX4 294
#define MODEL 295
#define MREF 296
#define NORMAL 297
#define NURBSCURVE 298
#define NURBSSURFACE 299
#define OBJECTTYPE 300
#define ORDER 301
#define OUTTANGENT 302
#define PATCH 303
#define POINTLIGHT 304
#define POLYGON 305
#define REF 306
#define RGBA 307
#define ROTATE 308
#define ROTX 309
#define ROTY 310
#define ROTZ 311
#define SANIM 312
#define SCALAR 313
#define SCALE 314
#define SEQUENCE 315
#define SHADING 316
#define SWITCH 317
#define SWITCHCONDITION 318
#define TABLE 319
#define TABLE_V 320
#define TAG 321
#define TANGENT 322
#define TEXLIST 323
#define TEXTURE 324
#define TLENGTHS 325
#define TRANSFORM 326
#define TRANSLATE 327
#define TREF 328
#define TRIANGLEFAN 329
#define TRIANGLESTRIP 330
#define TRIM 331
#define TXT 332
#define UKNOTS 333
#define UV 334
#define AUX 335
#define VKNOTS 336
#define VERTEX 337
#define VERTEXANIM 338
#define VERTEXPOOL 339
#define VERTEXREF 340
#define XFMANIM 341
#define XFMSANIM 342
#define START_EGG 343
#define START_GROUP_BODY 344
#define START_TEXTURE_BODY 345
#define START_PRIMITIVE_BODY 346



#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED

# define yystype YYSTYPE /* obsolescent; will be withdrawn */
# define YYSTYPE_IS_DECLARED 1
#endif

extern YYSTYPE eggyylval;

#ifdef YYPARSE_PARAM
#if defined __STDC__ || defined __cplusplus
int eggyyparse (void *YYPARSE_PARAM);
#else
int eggyyparse ();
#endif
#else /* ! YYPARSE_PARAM */
#if defined __STDC__ || defined __cplusplus
int eggyyparse (void);
#else
int eggyyparse ();
#endif
#endif /* ! YYPARSE_PARAM */

#endif /* !YY_EGGYY_BUILT_X64_TMP_PARSER_YXX_H_INCLUDED  */
