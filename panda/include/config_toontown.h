/**
 * TOONTOWN OFFLINE SOFTWARE
 * Copyright (c) The Toontown Offline Team.  All rights reserved.
 *
 * Use of this software by anyone other than those of the Toontown Offline team
 * is strictly prohibited without explicit permission from the Toontown Offline team.
 *
 * @file config_toontown.h
 * @author jwcotejr
 * @date 2019-01-19
 */

#ifndef __CONFIG_TOONTOWN_H__
#define __CONFIG_TOONTOWN_H__

#include "pandabase.h"
#include "dconfig.h"
#include "notifyCategoryProxy.h"

NotifyCategoryDecl(dna, EXPCL_DNA, EXPTP_DNA);

extern EXPCL_DNA void init_libtoontown();

#endif /* __CONFIG_TOONTOWN_H__ */
