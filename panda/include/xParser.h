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

#ifndef YY_XYY_BUILT_X64_TMP_XPARSER_YXX_H_INCLUDED
# define YY_XYY_BUILT_X64_TMP_XPARSER_YXX_H_INCLUDED
/* Enabling traces.  */
#ifndef YYDEBUG
# define YYDEBUG 0
#endif
#if YYDEBUG
extern int xyydebug;
#endif

/* Tokens.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
   /* Put the tokens into the symbol table, so that GDB and other debuggers
      know about them.  */
   enum yytokentype {
     TOKEN_NAME = 1,
     TOKEN_STRING = 2,
     TOKEN_INTEGER = 3,
     TOKEN_GUID = 5,
     TOKEN_INTEGER_LIST = 6,
     TOKEN_REALNUM_LIST = 7,
     TOKEN_OBRACE = 10,
     TOKEN_CBRACE = 11,
     TOKEN_OPAREN = 12,
     TOKEN_CPAREN = 13,
     TOKEN_OBRACKET = 14,
     TOKEN_CBRACKET = 15,
     TOKEN_OANGLE = 16,
     TOKEN_CANGLE = 17,
     TOKEN_DOT = 18,
     TOKEN_COMMA = 19,
     TOKEN_SEMICOLON = 20,
     TOKEN_TEMPLATE = 31,
     TOKEN_WORD = 40,
     TOKEN_DWORD = 41,
     TOKEN_FLOAT = 42,
     TOKEN_DOUBLE = 43,
     TOKEN_CHAR = 44,
     TOKEN_UCHAR = 45,
     TOKEN_SWORD = 46,
     TOKEN_SDWORD = 47,
     TOKEN_VOID = 48,
     TOKEN_LPSTR = 49,
     TOKEN_UNICODE = 50,
     TOKEN_CSTRING = 51,
     TOKEN_ARRAY = 52
   };
#endif
/* Tokens.  */
#define TOKEN_NAME 1
#define TOKEN_STRING 2
#define TOKEN_INTEGER 3
#define TOKEN_GUID 5
#define TOKEN_INTEGER_LIST 6
#define TOKEN_REALNUM_LIST 7
#define TOKEN_OBRACE 10
#define TOKEN_CBRACE 11
#define TOKEN_OPAREN 12
#define TOKEN_CPAREN 13
#define TOKEN_OBRACKET 14
#define TOKEN_CBRACKET 15
#define TOKEN_OANGLE 16
#define TOKEN_CANGLE 17
#define TOKEN_DOT 18
#define TOKEN_COMMA 19
#define TOKEN_SEMICOLON 20
#define TOKEN_TEMPLATE 31
#define TOKEN_WORD 40
#define TOKEN_DWORD 41
#define TOKEN_FLOAT 42
#define TOKEN_DOUBLE 43
#define TOKEN_CHAR 44
#define TOKEN_UCHAR 45
#define TOKEN_SWORD 46
#define TOKEN_SDWORD 47
#define TOKEN_VOID 48
#define TOKEN_LPSTR 49
#define TOKEN_UNICODE 50
#define TOKEN_CSTRING 51
#define TOKEN_ARRAY 52



#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED

# define yystype YYSTYPE /* obsolescent; will be withdrawn */
# define YYSTYPE_IS_DECLARED 1
#endif

extern YYSTYPE xyylval;

#ifdef YYPARSE_PARAM
#if defined __STDC__ || defined __cplusplus
int xyyparse (void *YYPARSE_PARAM);
#else
int xyyparse ();
#endif
#else /* ! YYPARSE_PARAM */
#if defined __STDC__ || defined __cplusplus
int xyyparse (void);
#else
int xyyparse ();
#endif
#endif /* ! YYPARSE_PARAM */

#endif /* !YY_XYY_BUILT_X64_TMP_XPARSER_YXX_H_INCLUDED  */
