# This file is used by various classes in test.unit_test.test_scrubber.py
# This file is NOT to be used for character processing in the Lexos app proper!

EE_HTML = {'&ae;': 'æ', '&d;': 'ð', '&t;': 'þ', '&e;': 'ę', '&AE;': 'Æ',
           '&D;': 'Ð', '&T;': 'Þ', '&#541;': 'ȝ', '&#540;': 'Ȝ', '&E;': 'Ę',
           '&amp;': '&', '&lt;': '<', '&gt;': '>', '&#383;': 'ſ'}

EE_HTML_KEYS = "&ae;&d;&t;&e;&AE;&D;&T;&#541;&#540;&E;&amp;&lt;&gt;&#383;"

EE_HTML_VALS = "æðþęÆÐÞȝȜĘ&<>ſ"

DOE_SGML = {'&ae;': 'æ', '&d;': 'ð', '&t;': 'þ', '&e;': 'ę', '&AE;': 'Æ',
            '&D;': 'Ð', '&T;': 'Þ', '&E;': 'Ę', '&oe;': 'œ', '&amp;': '⁊',
            '&egrave;': 'è', '&eacute;': 'é', '&auml;': 'ä', '&ouml;': 'ö',
            '&uuml;': 'ü', '&amacron;': 'ā', '&cmacron;': 'c̄',
            '&emacron;': 'ē', '&imacron;': 'ī', '&nmacron;': 'n̄',
            '&omacron;': 'ō', '&pmacron;': 'p̄', '&qmacron;': 'q̄',
            '&rmacron;': 'r̄', '&lt;': '<', '&gt;': '>', '&lbar;': 'ł',
            '&tbar;': 'ꝥ', '&bbar;': 'ƀ'}

DOE_SGML_KEYS = "&ae;&d;&t;&e;&AE;&D;&T;&E;&oe;&amp;&egrave;&eacute;&auml;" \
                "&ouml;&uuml;&amacron;&cmacron;&emacron;&imacron;&nmacron;" \
                "&omacron;&pmacron;&qmacron;&rmacron;&lt;&gt;&lbar;&tbar;" \
                "&bbar;"

DOE_SGML_VALS = "æðþęÆÐÞĘœ⁊èéäöüāc̄ēīn̄ōp̄q̄r̄<>łꝥƀ"

MUFI3 = {'&aenl;': '\ueee0', '&ascap;': 'ᴀ', '&ordf;': 'ª', '&aogon;': 'ą',
         '&Aogon;': 'Ą', '&acurl;': '\ue433', '&Acurl;': '\ue033',
         '&adotbl;': 'ạ', '&Adotbl;': 'Ạ', '&adot;': 'ȧ', '&Adot;': 'Ȧ',
         '&auml;': 'ä', '&Auml;': 'Ä', '&adiaguml;': '\ue8d5',
         '&adotbluml;': '\ue41d', '&aacute;': 'á', '&Aacute;': 'Á',
         '&aenlacute;': '\ueaf0', '&aogonacute;': '\ue404',
         '&Aogonacute;': '\ue004', '&adblac;': '\ue425', '&Adblac;': '\ue025',
         '&adotacute;': '\uebf5', '&Adotacute;': '\uebf4', '&agrave;': 'à',
         '&Agrave;': 'À', '&acirc;': 'â', '&Acirc;': 'Â',
         '&aumlcirc;': '\ue41a', '&aringcirc;': '\ue41f', '&atilde;': 'ã',
         '&Atilde;': 'Ã', '&aring;': 'å', '&Aring;': 'Å', '&ahook;': 'ả',
         '&Ahook;': 'Ả', '&abreve;': 'ă', '&Abreve;': 'Ă', '&amacr;': 'ā',
         '&Amacr;': 'Ā', '&amacrbreve;': '\ue410', '&Amacrbreve;': '\ue010',
         '&abreveacute;': 'ắ', '&Abreveacute;': 'Ắ', '&amacracute;': '\ue40a',
         '&Amacracute;': '\ue00a', '&aalig;': 'ꜳ', '&aacloselig;': '\uefa0',
         '&AAlig;': 'Ꜳ', '&aaligenl;': '\uefdf', '&aaligdotbl;': '\ueff3',
         '&AAligdotbl;': '\ueff2', '&aaligdot;': '\uefef',
         '&AAligdot;': '\uefee', '&aaliguml;': '\uefff',
         '&AAliguml;': '\ueffe', '&aaligacute;': '\uefe1',
         '&AAligacute;': '\uefe0', '&aaligdblac;': '\uefeb',
         '&AAligdblac;': '\uefea', '&aelig;': 'æ', '&AElig;': 'Æ',
         '&aeligenl;': '\ueaf1', '&aeligscap;': 'ᴁ', '&aeligred;': '\uf204',
         '&aeligcurl;': '\uebeb', '&AEligcurl;': '\uebea',
         '&aeligogon;': '\ue440', '&AEligogon;': '\ue040',
         '&aeligdotbl;': '\ue436', '&AEligdotbl;': '\ue036',
         '&aeligdot;': '\ue443', '&AEligdot;': '\ue043',
         '&aeliguml;': '\ue442', '&AEliguml;': '\ue042', '&aeligacute;': 'ǽ',
         '&AEligacute;': 'Ǽ', '&aeligogonacute;': '\ue8d3',
         '&aeligdblac;': '\ue441', '&AEligdblac;': '\ue041',
         '&aeligring;': '\ue8d1', '&aeligbreve;': '\ue43f',
         '&AEligbreve;': '\ue03f', '&aeligmacr;': 'ǣ', '&AEligmacr;': 'Ǣ',
         '&aeligmacrbreve;': '\ue43d', '&AEligmacrbreve;': '\ue03d',
         '&aeligmacracute;': '\ue43a', '&AEligmacracute;': '\ue03a',
         '&aflig;': '\uefa3', '&afinslig;': '\uefa4', '&aglig;': '\uefa5',
         '&allig;': '\uefa6', '&anlig;': '\uefa7', '&anscaplig;': '\uefa8',
         '&aolig;': 'ꜵ', '&AOlig;': 'Ꜵ', '&aoligenl;': '\uefde',
         '&aenlosmalllig;': '\ueaf2', '&aoligred;': '\uf206',
         '&AOligred;': '\uf205', '&aoligdotbl;': '\ueff5',
         '&AOligdotbl;': '\ueff4', '&aoligacute;': '\uefe3',
         '&AOligacute;': '\uefe2', '&aoligdblac;': '\uebc1',
         '&AOligdblac;': '\uebc0', '&aplig;': '\uefa9', '&arlig;': '\uefaa',
         '&arscaplig;': '\uefab', '&aulig;': 'ꜷ', '&AUlig;': 'Ꜷ',
         '&auligdotbl;': '\ueff7', '&AUligdotbl;': '\ueff6',
         '&auligacute;': '\uefe5', '&AUligacute;': '\uefe4', '&avlig;': 'ꜹ',
         '&AVlig;': 'Ꜹ', '&avligslash;': 'ꜻ', '&AVligslash;': 'Ꜻ',
         '&avligslashacute;': '\uebb1', '&AVligslashacute;': '\uebb0',
         '&avligogon;': '\uebf1', '&AVligogon;': '\uebf0',
         '&avligdotbl;': '\ueff9', '&AVligdotbl;': '\ueff8',
         '&avligacute;': '\uefe7', '&AVligacute;': '\uefe6',
         '&avligdblac;': '\uebc3', '&AVligdblac;': '\uebc2', '&aylig;': 'ꜽ',
         '&AYlig;': 'Ꜽ', '&ayligdotbl;': '\ueffb', '&AYligdotbl;': '\ueffa',
         '&ayligdot;': '\ueff1', '&AYligdot;': '\ueff0',
         '&athornlig;': '\uefac', '&aesup;': '\ue42c', '&Aesup;': '\ue02c',
         '&iesup;': '\ue54a', '&aosup;': '\ue42d', '&ausup;': '\ue8e1',
         '&avsup;': '\ue42e', '&aunc;': '\uf214', '&aopen;': '\uf202',
         '&ains;': '\uf200', '&Ains;': '\uf201', '&aneckless;': '\uf215',
         '&anecklesselig;': '\uefa1', '&AnecklessElig;': '\uefae',
         '&anecklessvlig;': '\uefa2', '&aclose;': '\uf203', '&Asqu;': '\uf13a',
         '&benl;': '\ueee1', '&bscap;': 'ʙ', '&bscapdot;': '\uebd0',
         '&bscapdotbl;': '\uef25', '&bdotbl;': 'ḅ', '&Bdotbl;': 'Ḅ',
         '&bdot;': 'ḃ', '&Bdot;': 'Ḃ', '&bacute;': '\ue444',
         '&Bacute;': '\ue044', '&bstrok;': 'ƀ', '&bovlmed;': '\ue44d',
         '&bblig;': '\ueec2', '&bglig;': '\ueec3', '&cenl;': '\ueee2',
         '&cscap;': 'ᴄ', '&ccedil;': 'ç', '&Ccedil;': 'Ç', '&cogon;': '\ue476',
         '&Cogon;': '\ue076', '&cdotbl;': '\ue466', '&Cdotbl;': '\ue066',
         '&cdot;': 'ċ', '&Cdot;': 'Ċ', '&cacute;': 'ć', '&Cacute;': 'Ć',
         '&Covlhigh;': '\uf7b5', '&cklig;': '\ueec4', '&ctlig;': '\ueec5',
         '&Csqu;': '\uf106', '&ccurl;': '\uf198', '&CONbase;': 'Ↄ',
         '&conbase;': 'ↄ', '&denl;': '\ueee3', '&dscap;': 'ᴅ', '&dstrok;': 'đ',
         '&Dstrok;': 'Đ', '&dovlmed;': '\ue491', '&dtailstrok;': 'ꝱ',
         '&dtail;': 'ɖ', '&dscapdot;': '\uebd2', '&ddotbl;': 'ḍ',
         '&Ddotbl;': 'Ḍ', '&dscapdotbl;': '\uef26', '&ddot;': 'ḋ',
         '&Ddot;': 'Ḋ', '&dacute;': '\ue477', '&Dacute;': '\ue077',
         '&eth;': 'ð', '&ETH;': 'Ð', '&ethenl;': '\ueee5', '&ethscap;': 'ᴆ',
         '&ethdotbl;': '\ue48f', '&ETHdotbl;': '\ue08f',
         '&Dovlhigh;': '\uf7b6', '&drotdrotlig;': '\ueec6', '&Drot;': 'Ꝺ',
         '&drot;': 'ꝺ', '&drotdot;': '\uebd1', '&drotacute;': '\uebb2',
         '&drotenl;': '\ueee4', '&dscript;': 'ẟ', '&dcurl;': '\uf193',
         '&eenl;': '\ueee6', '&escap;': 'ᴇ', '&eogon;': 'ę', '&Eogon;': 'Ę',
         '&ecurl;': '\ue4e9', '&Ecurl;': '\ue0e9', '&eogoncurl;': '\uebf3',
         '&Eogoncurl;': '\uebf2', '&edotbl;': 'ẹ', '&Edotbl;': 'Ẹ',
         '&eogondot;': '\ue4eb', '&Eogondot;': '\ue0eb',
         '&eogondotbl;': '\ue4e8', '&Eogondotbl;': '\ue0e8',
         '&eogonenl;': '\ueaf3', '&edot;': 'ė', '&Edot;': 'Ė', '&euml;': 'ë',
         '&Euml;': 'Ë', '&eumlmacr;': '\ue4cd', '&eacute;': 'é',
         '&Eacute;': 'É', '&eogonacute;': '\ue499', '&Eogonacute;': '\ue099',
         '&edotblacute;': '\ue498', '&edblac;': '\ue4d1', '&Edblac;': '\ue0d1',
         '&edotacute;': '\ue4c8', '&Edotacute;': '\ue0c8',
         '&eogondotacute;': '\ue4ec', '&Eogondotacute;': '\ue0ec',
         '&eogondblac;': '\ue4ea', '&Eogondblac;': '\ue0ea', '&egrave;': 'è',
         '&Egrave;': 'È', '&ecirc;': 'ê', '&Ecirc;': 'Ê',
         '&eogoncirc;': '\ue49f', '&ering;': '\ue4cf', '&ebreve;': 'ĕ',
         '&Ebreve;': 'Ĕ', '&emacr;': 'ē', '&Emacr;': 'Ē',
         '&eogonmacr;': '\ue4bc', '&Eogonmacr;': '\ue0bc',
         '&emacrbreve;': '\ue4b7', '&Emacrbreve;': '\ue0b7',
         '&emacracute;': 'ḗ', '&Emacracute;': 'Ḗ', '&eylig;': '\ueec7',
         '&eacombcirc;': '\uebbd', '&eucombcirc;': '\uebbe',
         '&easup;': '\ue4e1', '&Easup;': '\ue0e1', '&eesup;': '\ue8e2',
         '&eisup;': '\ue4e2', '&eosup;': '\ue8e3', '&evsup;': '\ue4e3',
         '&schwa;': 'ə', '&Eunc;': '\uf10a', '&Euncclose;': '\uf217',
         '&eunc;': '\uf218', '&eext;': '\uf219', '&etall;': '\uf21a',
         '&fenl;': '\ueee7', '&fscap;': 'ꜰ', '&fdotbl;': '\ue4ee',
         '&Fdotbl;': '\ue0ee', '&fdot;': 'ḟ', '&Fdot;': 'Ḟ',
         '&fscapdot;': '\uebd7', '&facute;': '\ue4f0', '&Facute;': '\ue0f0',
         '&faumllig;': '\ueec8', '&fflig;': 'ﬀ', '&filig;': 'ﬁ',
         '&fjlig;': '\ueec9', '&foumllig;': '\uf1bc', '&fllig;': 'ﬂ',
         '&frlig;': '\ueeca', '&ftlig;': '\ueecb', '&fuumllig;': '\ueecc',
         '&fylig;': '\ueecd', '&ffilig;': 'ﬃ', '&ffllig;': 'ﬄ',
         '&fftlig;': '\ueece', '&ffylig;': '\ueecf', '&ftylig;': '\ueed0',
         '&fturn;': 'ⅎ', '&Fturn;': 'Ⅎ', '&Frev;': 'ꟻ', '&fins;': 'ꝼ',
         '&Fins;': 'Ꝼ', '&finsenl;': '\ueeff', '&finsdot;': '\uebd4',
         '&Finsdot;': '\uebd3', '&finsdothook;': '\uf21c',
         '&finssemiclose;': '\uf21b', '&finssemiclosedot;': '\uebd5',
         '&finsclose;': '\uf207', '&finsclosedot;': '\uebd6',
         '&finsdotbl;': '\ue7e5', '&Finsdotbl;': '\ue3e5',
         '&finsacute;': '\uebb4', '&Finsacute;': '\uebb3', '&fcurl;': '\uf194',
         '&genl;': '\ueee8', '&gscap;': 'ɢ', '&gstrok;': 'ǥ', '&Gstrok;': 'Ǥ',
         '&gdotbl;': '\ue501', '&Gdotbl;': '\ue101', '&gscapdotbl;': '\uef27',
         '&gdot;': 'ġ', '&Gdot;': 'Ġ', '&gscapdot;': '\uef20', '&Gacute;': 'Ǵ',
         '&gacute;': 'ǵ', '&gglig;': '\ueed1', '&gdlig;': '\ueed2',
         '&gdrotlig;': '\ueed3', '&gethlig;': '\ueed4', '&golig;': '\ueede',
         '&gplig;': '\uead2', '&grlig;': '\uead0', '&gins;': 'ᵹ',
         '&Gins;': 'Ᵹ', '&ginsturn;': 'ꝿ', '&Ginsturn;': 'Ꝿ',
         '&Gsqu;': '\uf10e', '&gdivloop;': '\uf21d', '&glglowloop;': '\uf21e',
         '&gsmlowloop;': '\uf21f', '&gopen;': 'ɡ', '&gcurl;': '\uf196',
         '&henl;': '\ueee9', '&hscap;': 'ʜ', '&hhook;': 'ɦ', '&hstrok;': 'ħ',
         '&hovlmed;': '\ue517', '&hdotbl;': 'ḥ', '&Hdotbl;': 'Ḥ',
         '&Hdot;': 'ḣ', '&hdot;': 'Ḣ', '&hscapdot;': '\uebda',
         '&hacute;': '\ue516', '&Hacute;': '\ue116', '&hwair;': 'ƕ',
         '&HWAIR;': 'Ƕ', '&hslonglig;': '\uebad', '&hslongligbar;': '\ue7c7',
         '&hrarmlig;': '\ue8c3', '&Hrarmlig;': '\ue8c2', '&hhalf;': 'ⱶ',
         '&Hhalf;': 'Ⱶ', '&Hunc;': '\uf110', '&hrdes;': '\uf23a',
         '&ienl;': '\ueeea', '&iscap;': 'ɪ', '&inodot;': 'ı',
         '&inodotenl;': '\ueefd', '&Idot;': 'İ', '&istrok;': 'ɨ',
         '&iogon;': 'į', '&Iogon;': 'Į', '&icurl;': '\ue52a',
         '&Icurl;': '\ue12a', '&idotbl;': 'ị', '&Idotbl;': 'Ị',
         '&ibrevinvbl;': '\ue548', '&iuml;': 'ï', '&Iuml;': 'Ï',
         '&iacute;': 'í', '&Iacute;': 'Í', '&idblac;': '\ue543',
         '&Idblac;': '\ue143', '&idotacute;': '\uebf7',
         '&Idotacute;': '\uebf6', '&igrave;': 'ì', '&Igrave;': 'Ì',
         '&icirc;': 'î', '&Icirc;': 'Î', '&ihook;': 'ỉ', '&Ihook;': 'Ỉ',
         '&ibreve;': 'ĭ', '&Ibreve;': 'Ĭ', '&imacr;': 'ī', '&Imacr;': 'Ī',
         '&iovlmed;': '\ue550', '&Iovlhigh;': '\ue150',
         '&imacrbreve;': '\ue537', '&Imacrbreve;': '\ue137',
         '&imacracute;': '\ue535', '&Imacracute;': '\ue135', '&ijlig;': 'ĳ',
         '&IJlig;': 'Ĳ', '&iasup;': '\ue8e4', '&iosup;': '\ue8e5',
         '&iusup;': '\ue8e6', '&ivsup;': '\ue54b', '&ilong;': '\uf220',
         '&Ilong;': 'ꟾ', '&jenl;': '\ueeeb', '&jscap;': 'ᴊ', '&jnodot;': 'ȷ',
         '&jnodotenl;': '\ueefe', '&Jdot;': '\ue15c', '&jnodotstrok;': 'ɟ',
         '&jbar;': 'ɉ', '&Jbar;': 'Ɉ', '&jcurl;': '\ue563',
         '&Jcurl;': '\ue163', '&juml;': '\uebe3', '&Juml;': '\uebe2',
         '&jdotbl;': '\ue551', '&Jdotbl;': '\ue151', '&jacute;': '\ue553',
         '&Jacute;': '\ue153', '&jdblac;': '\ue562', '&Jdblac;': '\ue162',
         '&jmacrmed;': '\ue554', '&jovlmed;': '\ue552',
         '&Jmacrhigh;': '\ue154', '&Jovlhigh;': '\ue152', '&jesup;': '\ue8e7',
         '&kenl;': '\ueeec', '&kscap;': 'ᴋ', '&khook;': 'ƙ', '&kbar;': 'ꝁ',
         '&Kbar;': 'Ꝁ', '&kovlmed;': '\ue7c3', '&kstrleg;': 'ꝃ',
         '&Kstrleg;': 'Ꝃ', '&kstrascleg;': 'ꝅ', '&Kstrascleg;': 'Ꝅ',
         '&kdot;': '\ue568', '&Kdot;': '\ue168', '&kscapdot;': '\uebdb',
         '&kdotbl;': 'ḳ', '&Kdotbl;': 'Ḳ', '&kacute;': 'ḱ', '&Kacute;': 'Ḱ',
         '&kslonglig;': '\uebae', '&kslongligbar;': '\ue7c8',
         '&krarmlig;': '\ue8c5', '&kunc;': '\uf208', '&ksemiclose;': '\uf221',
         '&kclose;': '\uf209', '&kcurl;': '\uf195', '&lenl;': '\ueeed',
         '&lscap;': 'ʟ', '&lbar;': 'ƚ', '&lstrok;': 'ł', '&Lstrok;': 'Ł',
         '&lhighstrok;': 'ꝉ', '&Lhighstrok;': 'Ꝉ', '&lovlmed;': '\ue5b1',
         '&ltailstrok;': 'ꝲ', '&ldotbl;': 'ḷ', '&Ldotbl;': 'Ḷ',
         '&lscapdotbl;': '\uef28', '&ldot;': '\ue59e', '&Ldot;': '\ue19e',
         '&lscapdot;': '\uebdc', '&lacute;': 'ĺ', '&Lacute;': 'Ĺ',
         '&lringbl;': '\ue5a4', '&lmacrhigh;': '\ue596',
         '&lovlhigh;': '\ue58c', '&Lovlhigh;': '\uf7b4', '&lbrk;': 'ꝇ',
         '&Lbrk;': 'Ꝇ', '&llwelsh;': 'ỻ', '&LLwelsh;': 'Ỻ',
         '&lllig;': '\uf4f9', '&ldes;': '\uf222', '&lturn;': 'ꞁ',
         '&Lturn;': 'Ꞁ', '&menl;': '\ueeee', '&mscap;': 'ᴍ',
         '&mtailstrok;': 'ꝳ', '&mdotbl;': 'ṃ', '&Mdotbl;': 'Ṃ',
         '&mscapdotbl;': '\uef29', '&mdot;': 'ṁ', '&Mdot;': 'Ṁ',
         '&mscapdot;': '\uebdd', '&macute;': 'ḿ', '&Macute;': 'Ḿ',
         '&mringbl;': '\ue5c5', '&mmacrmed;': '\ue5b8',
         '&Mmacrhigh;': '\ue1b8', '&movlmed;': '\ue5d2',
         '&Movlhigh;': '\ue1d2', '&mesup;': '\ue8e8', '&Minv;': 'ꟽ',
         '&mrdes;': '\uf223', '&munc;': '\uf225', '&Munc;': '\uf11a',
         '&muncdes;': '\uf226', '&Muncdes;': '\uf224', '&muncacute;': '\uebb6',
         '&Muncacute;': '\uebb5', '&M5leg;': 'ꟿ', '&nenl;': '\ueeef',
         '&nscap;': 'ɴ', '&nscapldes;': '\uf22b', '&nlrleg;': 'ƞ',
         '&nlfhook;': 'ɲ', '&nbar;': '\ue7b2', '&ntailstrok;': 'ꝴ',
         '&ndot;': 'ṅ', '&Ndot;': 'Ṅ', '&nscapdot;': '\uef21', '&nacute;': 'ń',
         '&Nacute;': 'Ń', '&ndotbl;': 'ṇ', '&Ndotbl;': 'Ṇ',
         '&nscapdotbl;': '\uef2a', '&ncirc;': '\ue5d7', '&ntilde;': 'ñ',
         '&Ntilde;': 'Ñ', '&nringbl;': '\ue5ee', '&nmacrmed;': '\ue5dc',
         '&Nmacrhigh;': '\ue1dc', '&eng;': 'ŋ', '&ENG;': 'Ŋ',
         '&nscapslonglig;': '\ueed5', '&nrdes;': '\uf228', '&Nrdes;': '\uf229',
         '&nscaprdes;': '\uf22a', '&nflour;': '\uf19a', '&oenl;': '\ueef0',
         '&oscap;': 'ᴏ', '&ordm;': 'º', '&oogon;': 'ǫ', '&Oogon;': 'Ǫ',
         '&ocurl;': '\ue7d3', '&Ocurl;': '\ue3d3', '&oogoncurl;': '\ue64f',
         '&Oogoncurl;': '\ue24f', '&ocurlacute;': '\uebb8',
         '&Ocurlacute;': '\uebb7', '&oslash;': 'ø', '&Oslash;': 'Ø',
         '&oslashcurl;': '\ue7d4', '&Oslashcurl;': '\ue3d4',
         '&oslashogon;': '\ue655', '&Oslashogon;': '\ue255', '&odotbl;': 'ọ',
         '&Odotbl;': 'Ọ', '&oslashdotbl;': '\uebe1', '&Oslashdotbl;': '\uebe0',
         '&odot;': 'ȯ', '&Odot;': 'Ȯ', '&oogondot;': '\uebdf',
         '&Oogondot;': '\uebde', '&oogonmacr;': 'ǭ', '&Oogonmacr;': 'Ǭ',
         '&oslashdot;': '\uebce', '&Oslashdot;': '\uebcd',
         '&oogondotbl;': '\ue608', '&Oogondotbl;': '\ue208', '&ouml;': 'ö',
         '&Ouml;': 'Ö', '&odiaguml;': '\ue8d7', '&oumlacute;': '\ue62c',
         '&oacute;': 'ó', '&Oacute;': 'Ó', '&oslashacute;': 'ǿ',
         '&Oslashacute;': 'Ǿ', '&oslashdblac;': '\uebc7',
         '&Oslashdblac;': '\uebc6', '&oogonacute;': '\ue60c',
         '&Oogonacute;': '\ue20c', '&oslashogonacute;': '\ue657',
         '&Oslashogonacute;': '\ue257', '&odblac;': 'ő', '&Odblac;': 'Ő',
         '&odotacute;': '\uebf9', '&Odotacute;': '\uebf8',
         '&oogondotacute;': '\uebfb', '&Oogondotacute;': '\uebfa',
         '&oslashdotacute;': '\uebfd', '&Oslashdotacute;': '\uebfc',
         '&oogondblac;': '\uebc5', '&Oogondblac;': '\uebc4', '&ograve;': 'ò',
         '&Ograve;': 'Ò', '&ocirc;': 'ô', '&Ocirc;': 'Ô',
         '&oumlcirc;': '\ue62d', '&Oumlcirc;': '\ue22d',
         '&oogoncirc;': '\ue60e', '&ocar;': 'ǒ', '&Ocar;': 'Ǒ',
         '&otilde;': 'õ', '&Otilde;': 'Õ', '&oring;': '\ue637', '&ohook;': 'ỏ',
         '&Ohook;': 'Ỏ', '&obreve;': 'ŏ', '&Obreve;': 'Ŏ',
         '&oslashbreve;': '\uebef', '&Oslashbreve;': '\uebee', '&omacr;': 'ō',
         '&Omacr;': 'Ō', '&oslashmacr;': '\ue652', '&Oslashmacr;': '\ue252',
         '&omacrbreve;': '\ue61b', '&Omacrbreve;': '\ue21b',
         '&oslashmacrbreve;': '\ue653', '&Oslashmacrbreve;': '\ue253',
         '&omacracute;': 'ṓ', '&Omacracute;': 'Ṓ',
         '&oslashmacracute;': '\uebed', '&Oslashmacracute;': '\uebec',
         '&oumlmacr;': 'ȫ', '&Oumlmacr;': 'Ȫ', '&oclig;': '\uefad',
         '&oelig;': 'œ', '&OElig;': 'Œ', '&oeligscap;': 'ɶ',
         '&oeligenl;': '\uefdd', '&Oloop;': 'Ꝍ', '&oloop;': 'ꝍ',
         '&oeligacute;': '\ue659', '&OEligacute;': '\ue259',
         '&oeligdblac;': '\uebc9', '&OEligdblac;': '\uebc8',
         '&oeligmacr;': '\ue65d', '&OEligmacr;': '\ue25d',
         '&oeligmacrbreve;': '\ue660', '&OEligmacrbreve;': '\ue260',
         '&oolig;': 'ꝏ', '&OOlig;': 'Ꝏ', '&ooliguml;': '\uebe5',
         '&OOliguml;': '\uebe4', '&ooligacute;': '\uefe9',
         '&OOligacute;': '\uefe8', '&ooligdblac;': '\uefed',
         '&OOligdblac;': '\uefec', '&ooligdotbl;': '\ueffd',
         '&OOligdotbl;': '\ueffc', '&oasup;': '\ue643', '&oesup;': '\ue644',
         '&Oesup;': '\ue244', '&oisup;': '\ue645', '&oosup;': '\ue8e9',
         '&ousup;': '\ue646', '&Ousup;': '\ue246', '&ovsup;': '\ue647',
         '&oopen;': 'ɔ', '&oopenmacr;': '\ue7cc', '&penl;': '\ueef1',
         '&pscap;': 'ᴘ', '&pbardes;': 'ꝑ', '&Pbardes;': 'Ꝑ', '&pflour;': 'ꝓ',
         '&Pflour;': 'Ꝓ', '&psquirrel;': 'ꝕ', '&Psquirrel;': 'Ꝕ',
         '&pdotbl;': '\ue66d', '&Pdotbl;': '\ue26d', '&pdot;': 'ṗ',
         '&Pdot;': 'Ṗ', '&pscapdot;': '\uebcf', '&pacute;': 'ṕ',
         '&Pacute;': 'Ṕ', '&pmacr;': '\ue665', '&pplig;': '\ueed6',
         '&PPlig;': '\ueedd', '&ppflourlig;': '\ueed7', '&ppliguml;': '\uebe7',
         '&PPliguml;': '\uebe6', '&Prev;': 'ꟼ', '&qenl;': '\ueef2',
         '&qscap;': '\uef0c', '&qslstrok;': 'ꝙ', '&Qslstrok;': 'Ꝙ',
         '&qbardes;': 'ꝗ', '&Qbardes;': 'Ꝗ', '&qbardestilde;': '\ue68b',
         '&q2app;': '\ue8b3', '&q3app;': '\ue8bf', '&qcentrslstrok;': '\ue8b4',
         '&qdotbl;': '\ue688', '&Qdotbl;': '\ue288', '&qdot;': '\ue682',
         '&Qdot;': '\ue282', '&qmacr;': '\ue681', '&qvinslig;': '\uead1',
         '&Qstem;': '\uf22c', '&renl;': '\ueef3', '&rscap;': 'ʀ', '&YR;': 'Ʀ',
         '&rdes;': 'ɼ', '&rdesstrok;': '\ue7e4', '&rtailstrok;': 'ꝵ',
         '&rscaptailstrok;': 'ꝶ', '&Rtailstrok;': '℞', '&Rslstrok;': '℟',
         '&rdotbl;': 'ṛ', '&Rdotbl;': 'Ṛ', '&rdot;': 'ṙ', '&Rdot;': 'Ṙ',
         '&rscapdot;': '\uef22', '&racute;': 'ŕ', '&Racute;': 'Ŕ',
         '&rringbl;': '\ue6a3', '&rscapdotbl;': '\uef2b', '&resup;': '\ue8ea',
         '&rrot;': 'ꝛ', '&Rrot;': 'Ꝛ', '&rrotdotbl;': '\ue7c1',
         '&rrotacute;': '\uebb9', '&rins;': 'ꞃ', '&Rins;': 'Ꞃ',
         '&rflour;': '\uf19b', '&senl;': '\ueef4', '&sscap;': 'ꜱ',
         '&sdot;': 'ṡ', '&Sdot;': 'Ṡ', '&sscapdot;': '\uef23', '&sacute;': 'ś',
         '&Sacute;': 'Ś', '&sdotbl;': 'ṣ', '&Sdotbl;': 'Ṣ',
         '&sscapdotbl;': '\uef2c', '&szlig;': 'ß', '&SZlig;': 'ẞ',
         '&slongaumllig;': '\ueba0', '&slongchlig;': '\uf4fa',
         '&slonghlig;': '\ueba1', '&slongilig;': '\ueba2',
         '&slongjlig;': '\uf4fb', '&slongklig;': '\uf4fc',
         '&slongllig;': '\ueba3', '&slongoumllig;': '\ueba4',
         '&slongplig;': '\ueba5', '&slongslig;': '\uf4fd',
         '&slongslonglig;': '\ueba6', '&slongslongilig;': '\ueba7',
         '&slongslongklig;': '\uf4fe', '&slongslongllig;': '\ueba8',
         '&slongslongtlig;': '\uf4ff', '&stlig;': 'ﬆ', '&slongtlig;': 'ﬅ',
         '&slongtilig;': '\ueba9', '&slongtrlig;': '\uebaa',
         '&slonguumllig;': '\uebab', '&slongvinslig;': '\uebac',
         '&slongdestlig;': '\ueada', '&slong;': 'ſ', '&slongenl;': '\ueedf',
         '&slongbarslash;': 'ẜ', '&slongbar;': 'ẝ', '&slongovlmed;': '\ue79e',
         '&slongslstrok;': '\ue8b8', '&slongflour;': '\ue8b7',
         '&slongacute;': '\uebaf', '&slongdes;': '\uf127',
         '&slongdotbl;': '\ue7c2', '&Sclose;': '\uf126', '&sclose;': '\uf128',
         '&sins;': 'ꞅ', '&Sins;': 'Ꞅ', '&tenl;': '\ueef5', '&tscap;': 'ᴛ',
         '&ttailstrok;': 'ꝷ', '&togon;': '\ue6ee', '&Togon;': '\ue2ee',
         '&tdotbl;': 'ṭ', '&Tdotbl;': 'Ṭ', '&tdot;': 'ṫ', '&Tdot;': 'Ṫ',
         '&tscapdot;': '\uef24', '&tscapdotbl;': '\uef2d',
         '&tacute;': '\ue6e2', '&Tacute;': '\ue2e2', '&trlig;': '\ueed8',
         '&ttlig;': '\ueed9', '&trottrotlig;': '\ueeda', '&tylig;': '\ueedb',
         '&tzlig;': '\ueedc', '&trot;': 'ꞇ', '&Trot;': 'Ꞇ',
         '&tcurl;': '\uf199', '&uenl;': '\ueef7', '&uscap;': 'ᴜ',
         '&ubar;': 'ʉ', '&uogon;': 'ų', '&Uogon;': 'Ų', '&ucurl;': '\ue731',
         '&Ucurl;': '\ue331', '&udotbl;': 'ụ', '&Udotbl;': 'Ụ',
         '&ubrevinvbl;': '\ue727', '&udot;': '\ue715', '&Udot;': '\ue315',
         '&uuml;': 'ü', '&Uuml;': 'Ü', '&uacute;': 'ú', '&Uacute;': 'Ú',
         '&udblac;': 'ű', '&Udblac;': 'Ű', '&udotacute;': '\uebff',
         '&Udotacute;': '\uebfe', '&ugrave;': 'ù', '&Ugrave;': 'Ù',
         '&uvertline;': '\ue724', '&Uvertline;': '\ue324', '&ucirc;': 'û',
         '&Ucirc;': 'Û', '&uumlcirc;': '\ue717', '&Uumlcirc;': '\ue317',
         '&ucar;': 'ǔ', '&Ucar;': 'Ǔ', '&uring;': 'ů', '&Uring;': 'Ů',
         '&uhook;': 'ủ', '&Uhook;': 'Ủ', '&ucurlbar;': '\uebbf',
         '&ubreve;': 'ŭ', '&Ubreve;': 'Ŭ', '&umacr;': 'ū', '&Umacr;': 'Ū',
         '&umacrbreve;': '\ue70b', '&Umacrbreve;': '\ue30b',
         '&umacracute;': '\ue709', '&Umacracute;': '\ue309', '&uumlmacr;': 'ǖ',
         '&Uumlmacr;': 'Ǖ', '&uasup;': '\ue8eb', '&uesup;': '\ue72b',
         '&Uesup;': '\ue32b', '&uisup;': '\ue72c', '&uosup;': '\ue72d',
         '&Uosup;': '\ue32d', '&uvsup;': '\ue8ec', '&uwsup;': '\ue8ed',
         '&venl;': '\ueef8', '&vscap;': 'ᴠ', '&vbar;': '\ue74e',
         '&vslash;': '\ue8ba', '&vdiagstrok;': 'ꝟ', '&Vdiagstrok;': 'Ꝟ',
         '&Vslstrok;': '℣', '&vdotbl;': 'ṿ', '&Vdotbl;': 'Ṿ',
         '&vdot;': '\ue74c', '&Vdot;': '\ue34c', '&vuml;': '\ue742',
         '&Vuml;': '\ue342', '&vacute;': '\ue73a', '&Vacute;': '\ue33a',
         '&vdblac;': '\ue74b', '&Vdblac;': '\ue34b', '&vcirc;': '\ue73b',
         '&Vcirc;': '\ue33b', '&vring;': '\ue743', '&vmacr;': '\ue74d',
         '&Vmacr;': '\ue34d', '&Vovlhigh;': '\uf7b2', '&wynn;': 'ƿ',
         '&WYNN;': 'Ƿ', '&vins;': 'ꝩ', '&Vins;': 'Ꝩ', '&vinsdotbl;': '\ue7e6',
         '&Vinsdotbl;': '\ue3e6', '&vinsdot;': '\ue7e7', '&Vinsdot;': '\ue3e7',
         '&vinsacute;': '\uebbb', '&Vinsacute;': '\uebba', '&vwelsh;': 'ỽ',
         '&Vwelsh;': 'Ỽ', '&wenl;': '\ueef9', '&wscap;': 'ᴡ', '&wdotbl;': 'ẉ',
         '&Wdotbl;': 'Ẉ', '&wdot;': 'ẇ', '&Wdot;': 'Ẇ', '&wuml;': 'ẅ',
         '&Wuml;': 'Ẅ', '&wacute;': 'ẃ', '&Wacute;': 'Ẃ', '&wdblac;': '\ue750',
         '&Wdblac;': '\ue350', '&wgrave;': 'ẁ', '&Wgrave;': 'Ẁ',
         '&wcirc;': 'ŵ', '&Wcirc;': 'Ŵ', '&wring;': 'ẘ', '&wmacr;': '\ue757',
         '&Wmacr;': '\ue357', '&wasup;': '\ue8f0', '&wesup;': '\ue753',
         '&Wesup;': '\ue353', '&wisup;': '\ue8f1', '&wosup;': '\ue754',
         '&wusup;': '\ue8f2', '&wvsup;': '\ue8f3', '&xenl;': '\ueefa',
         '&xscap;': '\uef11', '&xmod;': 'ˣ', '&xslashula;': '\ue8bd',
         '&xslashlra;': '\ue8be', '&Xovlhigh;': '\uf7b3', '&xldes;': '\uf232',
         '&yenl;': '\ueefb', '&yscap;': 'ʏ', '&ybar;': '\ue77b',
         '&ycurl;': '\ue785', '&Ycurl;': '\ue385', '&ydotbl;': 'ỵ',
         '&Ydotbl;': 'Ỵ', '&ydot;': 'ẏ', '&Ydot;': 'Ẏ', '&yuml;': 'ÿ',
         '&Yuml;': 'Ÿ', '&yacute;': 'ý', '&Yacute;': 'Ý', '&ydblac;': '\ue77c',
         '&Ydblac;': '\ue37c', '&ydotacute;': '\ue784',
         '&Ydotacute;': '\ue384', '&ygrave;': 'ỳ', '&Ygrave;': 'Ỳ',
         '&ycirc;': 'ŷ', '&Ycirc;': 'Ŷ', '&yring;': 'ẙ', '&yhook;': 'ỷ',
         '&Yhook;': 'Ỷ', '&ybreve;': '\ue776', '&Ybreve;': '\ue376',
         '&ymacr;': 'ȳ', '&Ymacr;': 'Ȳ', '&ymacrbreve;': '\ue775',
         '&Ymacrbreve;': '\ue375', '&ymacracute;': '\ue773',
         '&Ymacracute;': '\ue373', '&yylig;': 'ꝡ', '&YYlig;': 'Ꝡ',
         '&yyliguml;': '\uebe9', '&YYliguml;': '\uebe8',
         '&yyligdblac;': '\uebcb', '&YYligdblac;': '\uebca',
         '&yesup;': '\ue781', '&yrgmainstrok;': '\uf233', '&yloop;': 'ỿ',
         '&Yloop;': 'Ỿ', '&zenl;': '\ueefc', '&zscap;': 'ᴢ', '&zstrok;': 'ƶ',
         '&Zstrok;': 'Ƶ', '&zdotbl;': 'ẓ', '&Zdotbl;': 'Ẓ', '&zdot;': 'ż',
         '&Zdot;': 'Ż', '&zvisigot;': 'ꝣ', '&Zvisigot;': 'Ꝣ', '&ezh;': 'ʒ',
         '&EZH;': 'Ʒ', '&yogh;': 'ȝ', '&YOGH;': 'Ȝ', '&thorn;': 'þ',
         '&THORN;': 'Þ', '&thornenl;': '\ueef6', '&thornscap;': '\uef15',
         '&thornbar;': 'ꝥ', '&THORNbar;': 'Ꝥ', '&thornovlmed;': '\ue7a2',
         '&thornbarslash;': '\uf149', '&THORNbarslash;': '\ue337',
         '&thornbardes;': 'ꝧ', '&THORNbardes;': 'Ꝧ', '&thorndotbl;': '\ue79f',
         '&THORNdotbl;': '\ue39f', '&thornacute;': '\ue737',
         '&thornslonglig;': '\ue734', '&thornslongligbar;': '\ue735',
         '&thornrarmlig;': '\ue8c1', '&frac14;': '¼', '&frac12;': '½',
         '&frac34;': '¾', '&sup0;': '⁰', '&sup1;': '¹', '&sup2;': '²',
         '&sup3;': '³', '&sup4;': '⁴', '&sup5;': '⁵', '&sup6;': '⁶',
         '&sup7;': '⁷', '&sup8;': '⁸', '&sup9;': '⁹', '&sub0;': '₀',
         '&sub1;': '₁', '&sub2;': '₂', '&sub3;': '₃', '&sub4;': '₄',
         '&sub5;': '₅', '&sub6;': '₆', '&sub7;': '₇', '&sub8;': '₈',
         '&sub9;': '₉', '&romnumCDlig;': 'ↀ', '&romnumDDlig;': 'ↁ',
         '&romnumDDdbllig;': 'ↂ', '&romnumCrev;': 'Ↄ',
         '&romnumCrevovl;': '\uf23f', '&Imod;': 'ᴵ', '&Vmod;': '\uf1be',
         '&Xmod;': '\uf1bf', '&asup;': 'ͣ', '&aeligsup;': 'ᷔ',
         '&anligsup;': '\uf036', '&anscapligsup;': '\uf03a', '&aoligsup;': 'ᷕ',
         '&arligsup;': '\uf038', '&arscapligsup;': '\uf130', '&avligsup;': 'ᷖ',
         '&bsup;': '\uf012', '&bscapsup;': '\uf013', '&csup;': 'ͨ',
         '&ccedilsup;': 'ᷗ', '&dsup;': 'ͩ', '&drotsup;': 'ᷘ', '&ethsup;': 'ᷙ',
         '&dscapsup;': '\uf016', '&esup;': 'ͤ', '&eogonsup;': '\uf135',
         '&emacrsup;': '\uf136', '&fsup;': '\uf017', '&gsup;': 'ᷚ',
         '&gscapsup;': 'ᷛ', '&hsup;': 'ͪ', '&isup;': 'ͥ',
         '&inodotsup;': '\uf02f', '&jsup;': '\uf030', '&jnodotsup;': '\uf031',
         '&ksup;': 'ᷜ', '&kscapsup;': '\uf01c', '&lsup;': 'ᷝ',
         '&lscapsup;': 'ᷞ', '&msup;': 'ͫ', '&mscapsup;': 'ᷟ', '&nsup;': 'ᷠ',
         '&nscapsup;': 'ᷡ', '&osup;': 'ͦ', '&omacrsup;': '\uf13f',
         '&oslashsup;': '\uf032', '&oogonsup;': '\uf13e',
         '&orrotsup;': '\uf03e', '&orumsup;': '\uf03f', '&psup;': '\uf025',
         '&qsup;': '\uf033', '&rsup;': 'ͬ', '&rrotsup;': 'ᷣ',
         '&rumsup;': '\uf040', '&rscapsup;': 'ᷢ', '&ssup;': 'ᷤ',
         '&slongsup;': 'ᷥ', '&tsup;': 'ͭ', '&trotsup;': '\uf03b',
         '&tscapsup;': '\uf02a', '&usup;': 'ͧ', '&vsup;': 'ͮ',
         '&wsup;': '\uf03c', '&xsup;': 'ͯ', '&ysup;': '\uf02b', '&zsup;': 'ᷦ',
         '&thornsup;': '\uf03d', '&combgrave;': '̀', '&combacute;': '́',
         '&combcirc;': '̂', '&combcircdbl;': '᷍', '&combtilde;': '̃',
         '&combmacr;': '̄', '&combbreve;': '̆', '&combdot;': '̇',
         '&combuml;': '̈', '&combhook;': '̉', '&combring;': '̊',
         '&combdblac;': '̋', '&combsgvertl;': '̍', '&combdbvertl;': '̎',
         '&combdotbl;': '̣', '&combced;': '̧', '&dblbarbl;': '̳',
         '&dblovl;': '̿', '&combogon;': '̨', '&combastbl;': '͙',
         '&combdblbrevebl;': '͜', '&combtripbrevebl;': '\uf1fc',
         '&combcurl;': '᷎', '&combcurlhigh;': '\uf1c5',
         '&combdothigh;': '\uf1ca', '&combcurlbar;': '\uf1cc', '&bar;': '̅',
         '&macrhigh;': '\uf00a', '&macrmed;': '\uf00b', '&ovlhigh;': '\uf00c',
         '&ovlmed;': '\uf00d', '&barbl;': '̲', '&baracr;': '̶',
         '&arbar;': '\uf1c0', '&combcomma;': '̕', '&combtildevert;': '̾',
         '&er;': '͛', '&erang;': '\uf1c7', '&ercurl;': '\uf1c8',
         '&ersub;': '᷏', '&ra;': 'ᷓ', '&rabar;': '\uf1c1', '&urrot;': '\uf153',
         '&urlemn;': '\uf1c2', '&ur;': '᷑', '&us;': '᷒', '&combisbelow;': '᷐',
         '&period;': '.', '&semi;': ';', '&amp;': '&', '&Theta;': 'Θ',
         '&theta;': 'θ', '&obiit;': 'ꝋ', '&OBIIT;': 'Ꝋ', '&et;': '⁊',
         '&etslash;': '\uf158', '&ET;': '\uf142', '&ETslash;': '\uf1a7',
         '&apomod;': 'ʼ', '&esse;': '≈', '&est;': '∻', '&condes;': 'ꝯ',
         '&CONdes;': 'Ꝯ', '&condot;': 'ꜿ', '&CONdot;': 'Ꜿ',
         '&usbase;': '\uf1a6', '&USbase;': '\uf1a5', '&usmod;': 'ꝰ',
         '&rum;': 'ꝝ', '&RUM;': 'Ꝝ', '&de;': '\uf159', '&is;': 'ꝭ',
         '&IS;': 'Ꝭ', '&sstrok;': 'ꝸ', '&etfin;': 'ꝫ', '&ETfin;': 'Ꝫ',
         '&sem;': '\uf1ac', '&fMedrun;': 'ᚠ', '&mMedrun;': 'ᛘ', '&lbbar;': '℔',
         '&circ;': '^', '&acute;': '´', '&grave;': '`', '&uml;': '¨',
         '&tld;': '~', '&macr;': '¯', '&breve;': '˘', '&dot;': '˙',
         '&ring;': '˚', '&cedil;': '¸', '&ogon;': '˛', '&tilde;': '˜',
         '&dblac;': '˝', '&verbarup;': 'ˈ', '&middot;': '·',
         '&hyphpoint;': '‧', '&sgldr;': '․', '&dblldr;': '‥', '&hellip;': '…',
         '&colon;': ':', '&comma;': ',', '&tridotright;': '჻',
         '&tridotupw;': '∴', '&tridotdw;': '∵', '&quaddot;': '∷',
         '&lozengedot;': '⁘', '&midring;': '\uf1da', '&verbar;': '|',
         '&brvbar;': '¦', '&Verbar;': '‖', '&sol;': '/', '&fracsol;': '⁄',
         '&dblsol;': '⫽', '&bsol;': '\\', '&luslst;': '⸌', '&ruslst;': '⸍',
         '&rlslst;': '⸜', '&llslst;': '⸝', '&lowbar;': '_', '&hyphen;': '-',
         '&dash;': '‐', '&nbhy;': '‑', '&dbloblhyph;': '⸗', '&numdash;': '‒',
         '&ndash;': '–', '&mdash;': '—', '&horbar;': '―', '&excl;': '!',
         '&iexcl;': '¡', '&quest;': '?', '&iquest;': '¿', '&ramus;': '\uf1db',
         '&lpar;': '(', '&rpar;': ')', '&lUbrack;': '⸦', '&rUbrack;': '⸧',
         '&ldblpar;': '⸨', '&rdblpar;': '⸩', '&lsqb;': '[', '&rsqb;': ']',
         '&lcub;': '{', '&rcub;': '}', '&lsqbqu;': '⁅', '&rsqbqu;': '⁆',
         '&lwhsqb;': '⟦', '&rwhsqb;': '⟧', '&verbarql;': '⸡',
         '&verbarqr;': '⸠', '&luhsqb;': '⸢', '&ruhsqb;': '⸣', '&llhsqb;': '⸤',
         '&rlhsqb;': '⸥', '&apos;': "'", '&prime;': '′', '&quot;': '"',
         '&Prime;': '″', '&lsquo;': '‘', '&rsquo;': '’', '&lsquolow;': '‚',
         '&rsquorev;': '‛', '&ldquo;': '“', '&rdquo;': '”', '&ldquolow;': '„',
         '&rdquorev;': '‟', '&lsaquo;': '‹', '&laquo;': '«', '&lt;': '<',
         '&langb;': '⟨', '&rsaquo;': '›', '&gt;': '>', '&raquo;': '»',
         '&rangb;': '⟩', '&hidot;': '\uf1f8', '&posit;': '\uf1e2',
         '&ductsimpl;': '\uf1e3', '&punctvers;': '\uf1ea',
         '&punctposit;': '\uf1e4', '&colmidcomposit;': '\uf1e5',
         '&bidotscomposit;': '\uf1f2', '&tridotscomposit;': '\uf1e6',
         '&punctelev;': '\uf161', '&punctelevdiag;': '\uf1f0',
         '&punctelevhiback;': '\uf1fa', '&punctelevhack;': '\uf1fb',
         '&punctflex;': '\uf1f5', '&punctexclam;': '\uf1e7',
         '&punctinter;': '\uf160', '&punctintertilde;': '\uf1e8',
         '&punctinterlemn;': '\uf1f1', '&punctpercont;': '⸮',
         '&wavylin;': '\uf1f9', '&medcom;': '\uf1e0', '&parag;': '\uf1e1',
         '&renvoi;': '\uf1ec', '&tridotsdownw;': '⸪', '&tridotsupw;': '⸫',
         '&quaddots;': '⸬', '&fivedots;': '⸭', '&virgsusp;': '\uf1f4',
         '&virgmin;': '\uf1f7', '&dipledot;': '⋗', '&sp;': ' ',
         '&nbsp;': '\xa0', '&nnbsp;': '\u202f', '&enqd;': '\u2000',
         '&emqd;': '\u2001', '&ensp;': '\u2002', '&emsp;': '\u2003',
         '&emsp13;': '\u2004', '&emsp14;': '\u2005', '&emsp16;': '\u2006',
         '&numsp;': '\u2007', '&puncsp;': '\u2008', '&thinsp;': '\u2009',
         '&hairsp;': '\u200a', '&zerosp;': '\u200b', '&del;': '\x7f',
         '&shy;': '\xad', '&num;': '#', '&sect;': '§', '&ast;': '*',
         '&triast;': '⁂', '&commat;': '@', '&copy;': '©', '&reg;': '®',
         '&not;': '¬', '&logand;': '∧', '&para;': '¶', '&revpara;': '⁋',
         '&cross;': '✝', '&dagger;': '†', '&Dagger;': '‡', '&refmark;': '※',
         '&dotcross;': '⁜', '&hedera;': '❦', '&hederarot;': '❧',
         '&dollar;': '$', '&cent;': '¢', '&pound;': '£', '&curren;': '¤',
         '&yen;': '¥', '&pennygerm;': '₰', '&scruple;': '℈',
         '&romaslibr;': '\uf2e0', '&romXbar;': '\uf2e1',
         '&romscapxbar;': '\uf2e2', '&romscapybar;': '\uf2e3',
         '&romscapdslash;': '\uf2e4', '&drotbar;': '\uf159', '&ecu;': '\uf2e7',
         '&florloop;': '\uf2e8', '&grosch;': '\uf2e9', '&libradut;': '\uf2ea',
         '&librafren;': '\uf2eb', '&libraital;': '\uf2ec',
         '&libraflem;': '\uf2ed', '&liranuov;': '\uf2ee',
         '&lirasterl;': '\uf2ef', '&markold;': '\uf2f0',
         '&markflour;': '\uf2f1', '&msign;': '\uf2f2',
         '&msignflour;': '\uf2f3', '&penningar;': '\uf2f5',
         '&reichtalold;': '\uf2f6', '&schillgerm;': '\uf2f7',
         '&schillgermscript;': '\uf2f8', '&scudi;': '\uf2f9', '&ounce;': '℥',
         '&sestert;': '\uf2fa', '&romas;': '\uf2d8', '&romunc;': '\uf2d9',
         '&romsemunc;': '\uf2da', '&romsext;': '\uf2db',
         '&romdimsext;': '\uf2dc', '&romsiliq;': '\uf2dd',
         '&romquin;': '\uf2de', '&romdupond;': '\uf2df', '&plus;': '+',
         '&minus;': '−', '&plusmn;': '±', '&times;': '×', '&divide;': '÷',
         '&equals;': '=', '&infin;': '∞', '&notequals;': '≠', '&percnt;': '%',
         '&permil;': '‰', '&deg;': '°', '&smallzero;': '\uf1bd',
         '&micro;': 'µ', '&dram;': '\uf2e6', '&obol;': '\uf2f4',
         '&sextans;': '\uf2fb', '&ouncescript;': '\uf2fd', '&arrsgllw;': '←',
         '&arrsglupw;': '↑', '&arrsglrw;': '→', '&arrsgldw;': '↓',
         '&squareblsm;': '▪', '&squarewhsm;': '▫', '&bull;': '•',
         '&circledot;': '◌', '&tribull;': '‣', '&trirightwh;': '▹',
         '&trileftwh;': '◃', '&metrshort;': '⏑', '&metrshortlong;': '⏒',
         '&metrlongshort;': '⏓', '&metrdblshortlong;': '⏔',
         '&metranc;': '\uf70a', '&metrancACUTE;': '\uf70b',
         '&metrancdblac;': '\uf719', '&metrancgrave;': '\uf70c',
         '&metrancdblgrave;': '\uf71a', '&metrbreve;': '\uf701',
         '&metrbreveacute;': '\uf706', '&metrbrevedblac;': '\uf717',
         '&metrbrevegrave;': '\uf707', '&metrbrevedblgrave;': '\uf718',
         '&metrmacr;': '\uf700', '&metrmacracute;': '\uf704',
         '&metrmacrdblac;': '\uf715', '&metrmacrgrave;': '\uf705',
         '&metrmacrdblgrave;': '\uf716', '&metrmacrbreve;': '\uf702',
         '&metrbrevemacr;': '\uf703', '&metrmacrbreveacute;': '\uf708',
         '&metrmacrbrevegrave;': '\uf709', '&metrdblbrevemacr;': '\uf72e',
         '&metrdblbrevemacracute;': '\uf71b',
         '&metrdblbrevemacrdblac;': '\uf71c', '&metrpause;': '\uf714'}

MUFI3_KEYS = "&aenl;&ascap;&ordf;&aogon;&Aogon;&acurl;&Acurl;&adotbl;" \
             "&Adotbl;&adot;&Adot;&auml;&Auml;&adiaguml;&adotbluml;&aacute;" \
             "&Aacute;&aenlacute;&aogonacute;&Aogonacute;&adblac;&Adblac;" \
             "&adotacute;&Adotacute;&agrave;&Agrave;&acirc;&Acirc;&aumlcirc;" \
             "&aringcirc;&atilde;&Atilde;&aring;&Aring;&ahook;&Ahook;" \
             "&abreve;&Abreve;&amacr;&Amacr;&amacrbreve;&Amacrbreve;" \
             "&abreveacute;&Abreveacute;&amacracute;&Amacracute;&aalig;" \
             "&aacloselig;&AAlig;&aaligenl;&aaligdotbl;&AAligdotbl;" \
             "&aaligdot;&AAligdot;&aaliguml;&AAliguml;&aaligacute;" \
             "&AAligacute;&aaligdblac;&AAligdblac;&aelig;&AElig;&aeligenl;" \
             "&aeligscap;&aeligred;&aeligcurl;&AEligcurl;&aeligogon;" \
             "&AEligogon;&aeligdotbl;&AEligdotbl;&aeligdot;&AEligdot;" \
             "&aeliguml;&AEliguml;&aeligacute;&AEligacute;&aeligogonacute;" \
             "&aeligdblac;&AEligdblac;&aeligring;&aeligbreve;&AEligbreve;" \
             "&aeligmacr;&AEligmacr;&aeligmacrbreve;&AEligmacrbreve;" \
             "&aeligmacracute;&AEligmacracute;&aflig;&afinslig;&aglig;" \
             "&allig;&anlig;&anscaplig;&aolig;&AOlig;&aoligenl;" \
             "&aenlosmalllig;&aoligred;&AOligred;&aoligdotbl;&AOligdotbl;" \
             "&aoligacute;&AOligacute;&aoligdblac;&AOligdblac;&aplig;&arlig;" \
             "&arscaplig;&aulig;&AUlig;&auligdotbl;&AUligdotbl;&auligacute;" \
             "&AUligacute;&avlig;&AVlig;&avligslash;&AVligslash;" \
             "&avligslashacute;&AVligslashacute;&avligogon;&AVligogon;" \
             "&avligdotbl;&AVligdotbl;&avligacute;&AVligacute;&avligdblac;" \
             "&AVligdblac;&aylig;&AYlig;&ayligdotbl;&AYligdotbl;&ayligdot;" \
             "&AYligdot;&athornlig;&aesup;&Aesup;&iesup;&aosup;&ausup;" \
             "&avsup;&aunc;&aopen;&ains;&Ains;&aneckless;&anecklesselig;" \
             "&AnecklessElig;&anecklessvlig;&aclose;&Asqu;&benl;&bscap;" \
             "&bscapdot;&bscapdotbl;&bdotbl;&Bdotbl;&bdot;&Bdot;&bacute;" \
             "&Bacute;&bstrok;&bovlmed;&bblig;&bglig;&cenl;&cscap;&ccedil;" \
             "&Ccedil;&cogon;&Cogon;&cdotbl;&Cdotbl;&cdot;&Cdot;&cacute;" \
             "&Cacute;&Covlhigh;&cklig;&ctlig;&Csqu;&ccurl;&CONbase;" \
             "&conbase;&denl;&dscap;&dstrok;&Dstrok;&dovlmed;&dtailstrok;" \
             "&dtail;&dscapdot;&ddotbl;&Ddotbl;&dscapdotbl;&ddot;&Ddot;" \
             "&dacute;&Dacute;&eth;&ETH;&ethenl;&ethscap;&ethdotbl;" \
             "&ETHdotbl;&Dovlhigh;&drotdrotlig;&Drot;&drot;&drotdot;" \
             "&drotacute;&drotenl;&dscript;&dcurl;&eenl;&escap;&eogon;" \
             "&Eogon;&ecurl;&Ecurl;&eogoncurl;&Eogoncurl;&edotbl;&Edotbl;" \
             "&eogondot;&Eogondot;&eogondotbl;&Eogondotbl;&eogonenl;&edot;" \
             "&Edot;&euml;&Euml;&eumlmacr;&eacute;&Eacute;&eogonacute;" \
             "&Eogonacute;&edotblacute;&edblac;&Edblac;&edotacute;" \
             "&Edotacute;&eogondotacute;&Eogondotacute;&eogondblac;" \
             "&Eogondblac;&egrave;&Egrave;&ecirc;&Ecirc;&eogoncirc;&ering;" \
             "&ebreve;&Ebreve;&emacr;&Emacr;&eogonmacr;&Eogonmacr;" \
             "&emacrbreve;&Emacrbreve;&emacracute;&Emacracute;&eylig;" \
             "&eacombcirc;&eucombcirc;&easup;&Easup;&eesup;&eisup;&eosup;" \
             "&evsup;&schwa;&Eunc;&Euncclose;&eunc;&eext;&etall;&fenl;" \
             "&fscap;&fdotbl;&Fdotbl;&fdot;&Fdot;&fscapdot;&facute;&Facute;" \
             "&faumllig;&fflig;&filig;&fjlig;&foumllig;&fllig;&frlig;&ftlig;" \
             "&fuumllig;&fylig;&ffilig;&ffllig;&fftlig;&ffylig;&ftylig;" \
             "&fturn;&Fturn;&Frev;&fins;&Fins;&finsenl;&finsdot;&Finsdot;" \
             "&finsdothook;&finssemiclose;&finssemiclosedot;&finsclose;" \
             "&finsclosedot;&finsdotbl;&Finsdotbl;&finsacute;&Finsacute;" \
             "&fcurl;&genl;&gscap;&gstrok;&Gstrok;&gdotbl;&Gdotbl;" \
             "&gscapdotbl;&gdot;&Gdot;&gscapdot;&Gacute;&gacute;&gglig;" \
             "&gdlig;&gdrotlig;&gethlig;&golig;&gplig;&grlig;&gins;&Gins;" \
             "&ginsturn;&Ginsturn;&Gsqu;&gdivloop;&glglowloop;&gsmlowloop;" \
             "&gopen;&gcurl;&henl;&hscap;&hhook;&hstrok;&hovlmed;&hdotbl;" \
             "&Hdotbl;&Hdot;&hdot;&hscapdot;&hacute;&Hacute;&hwair;&HWAIR;" \
             "&hslonglig;&hslongligbar;&hrarmlig;&Hrarmlig;&hhalf;&Hhalf;" \
             "&Hunc;&hrdes;&ienl;&iscap;&inodot;&inodotenl;&Idot;&istrok;" \
             "&iogon;&Iogon;&icurl;&Icurl;&idotbl;&Idotbl;&ibrevinvbl;&iuml;" \
             "&Iuml;&iacute;&Iacute;&idblac;&Idblac;&idotacute;&Idotacute;" \
             "&igrave;&Igrave;&icirc;&Icirc;&ihook;&Ihook;&ibreve;&Ibreve;" \
             "&imacr;&Imacr;&iovlmed;&Iovlhigh;&imacrbreve;&Imacrbreve;" \
             "&imacracute;&Imacracute;&ijlig;&IJlig;&iasup;&iosup;&iusup;" \
             "&ivsup;&ilong;&Ilong;&jenl;&jscap;&jnodot;&jnodotenl;&Jdot;" \
             "&jnodotstrok;&jbar;&Jbar;&jcurl;&Jcurl;&juml;&Juml;&jdotbl;" \
             "&Jdotbl;&jacute;&Jacute;&jdblac;&Jdblac;&jmacrmed;&jovlmed;" \
             "&Jmacrhigh;&Jovlhigh;&jesup;&kenl;&kscap;&khook;&kbar;&Kbar;" \
             "&kovlmed;&kstrleg;&Kstrleg;&kstrascleg;&Kstrascleg;&kdot;" \
             "&Kdot;&kscapdot;&kdotbl;&Kdotbl;&kacute;&Kacute;&kslonglig;" \
             "&kslongligbar;&krarmlig;&kunc;&ksemiclose;&kclose;&kcurl;" \
             "&lenl;&lscap;&lbar;&lstrok;&Lstrok;&lhighstrok;&Lhighstrok;" \
             "&lovlmed;&ltailstrok;&ldotbl;&Ldotbl;&lscapdotbl;&ldot;&Ldot;" \
             "&lscapdot;&lacute;&Lacute;&lringbl;&lmacrhigh;&lovlhigh;" \
             "&Lovlhigh;&lbrk;&Lbrk;&llwelsh;&LLwelsh;&lllig;&ldes;&lturn;" \
             "&Lturn;&menl;&mscap;&mtailstrok;&mdotbl;&Mdotbl;&mscapdotbl;" \
             "&mdot;&Mdot;&mscapdot;&macute;&Macute;&mringbl;&mmacrmed;" \
             "&Mmacrhigh;&movlmed;&Movlhigh;&mesup;&Minv;&mrdes;&munc;&Munc;" \
             "&muncdes;&Muncdes;&muncacute;&Muncacute;&M5leg;&nenl;&nscap;" \
             "&nscapldes;&nlrleg;&nlfhook;&nbar;&ntailstrok;&ndot;&Ndot;" \
             "&nscapdot;&nacute;&Nacute;&ndotbl;&Ndotbl;&nscapdotbl;&ncirc;" \
             "&ntilde;&Ntilde;&nringbl;&nmacrmed;&Nmacrhigh;&eng;&ENG;" \
             "&nscapslonglig;&nrdes;&Nrdes;&nscaprdes;&nflour;&oenl;&oscap;" \
             "&ordm;&oogon;&Oogon;&ocurl;&Ocurl;&oogoncurl;&Oogoncurl;" \
             "&ocurlacute;&Ocurlacute;&oslash;&Oslash;&oslashcurl;" \
             "&Oslashcurl;&oslashogon;&Oslashogon;&odotbl;&Odotbl;" \
             "&oslashdotbl;&Oslashdotbl;&odot;&Odot;&oogondot;&Oogondot;" \
             "&oogonmacr;&Oogonmacr;&oslashdot;&Oslashdot;&oogondotbl;" \
             "&Oogondotbl;&ouml;&Ouml;&odiaguml;&oumlacute;&oacute;&Oacute;" \
             "&oslashacute;&Oslashacute;&oslashdblac;&Oslashdblac;" \
             "&oogonacute;&Oogonacute;&oslashogonacute;&Oslashogonacute;" \
             "&odblac;&Odblac;&odotacute;&Odotacute;&oogondotacute;" \
             "&Oogondotacute;&oslashdotacute;&Oslashdotacute;&oogondblac;" \
             "&Oogondblac;&ograve;&Ograve;&ocirc;&Ocirc;&oumlcirc;&Oumlcirc;" \
             "&oogoncirc;&ocar;&Ocar;&otilde;&Otilde;&oring;&ohook;&Ohook;" \
             "&obreve;&Obreve;&oslashbreve;&Oslashbreve;&omacr;&Omacr;" \
             "&oslashmacr;&Oslashmacr;&omacrbreve;&Omacrbreve;" \
             "&oslashmacrbreve;&Oslashmacrbreve;&omacracute;&Omacracute;" \
             "&oslashmacracute;&Oslashmacracute;&oumlmacr;&Oumlmacr;&oclig;" \
             "&oelig;&OElig;&oeligscap;&oeligenl;&Oloop;&oloop;&oeligacute;" \
             "&OEligacute;&oeligdblac;&OEligdblac;&oeligmacr;&OEligmacr;" \
             "&oeligmacrbreve;&OEligmacrbreve;&oolig;&OOlig;&ooliguml;" \
             "&OOliguml;&ooligacute;&OOligacute;&ooligdblac;&OOligdblac;" \
             "&ooligdotbl;&OOligdotbl;&oasup;&oesup;&Oesup;&oisup;&oosup;" \
             "&ousup;&Ousup;&ovsup;&oopen;&oopenmacr;&penl;&pscap;&pbardes;" \
             "&Pbardes;&pflour;&Pflour;&psquirrel;&Psquirrel;&pdotbl;" \
             "&Pdotbl;&pdot;&Pdot;&pscapdot;&pacute;&Pacute;&pmacr;&pplig;" \
             "&PPlig;&ppflourlig;&ppliguml;&PPliguml;&Prev;&qenl;&qscap;" \
             "&qslstrok;&Qslstrok;&qbardes;&Qbardes;&qbardestilde;&q2app;" \
             "&q3app;&qcentrslstrok;&qdotbl;&Qdotbl;&qdot;&Qdot;&qmacr;" \
             "&qvinslig;&Qstem;&renl;&rscap;&YR;&rdes;&rdesstrok;" \
             "&rtailstrok;&rscaptailstrok;&Rtailstrok;&Rslstrok;&rdotbl;" \
             "&Rdotbl;&rdot;&Rdot;&rscapdot;&racute;&Racute;&rringbl;" \
             "&rscapdotbl;&resup;&rrot;&Rrot;&rrotdotbl;&rrotacute;&rins;" \
             "&Rins;&rflour;&senl;&sscap;&sdot;&Sdot;&sscapdot;&sacute;" \
             "&Sacute;&sdotbl;&Sdotbl;&sscapdotbl;&szlig;&SZlig;" \
             "&slongaumllig;&slongchlig;&slonghlig;&slongilig;&slongjlig;" \
             "&slongklig;&slongllig;&slongoumllig;&slongplig;&slongslig;" \
             "&slongslonglig;&slongslongilig;&slongslongklig;" \
             "&slongslongllig;&slongslongtlig;&stlig;&slongtlig;&slongtilig;" \
             "&slongtrlig;&slonguumllig;&slongvinslig;&slongdestlig;" \
             "&slong;&slongenl;&slongbarslash;&slongbar;&slongovlmed;" \
             "&slongslstrok;&slongflour;&slongacute;&slongdes;&slongdotbl;" \
             "&Sclose;&sclose;&sins;&Sins;&tenl;&tscap;&ttailstrok;&togon;" \
             "&Togon;&tdotbl;&Tdotbl;&tdot;&Tdot;&tscapdot;&tscapdotbl;" \
             "&tacute;&Tacute;&trlig;&ttlig;&trottrotlig;&tylig;&tzlig;" \
             "&trot;&Trot;&tcurl;&uenl;&uscap;&ubar;&uogon;&Uogon;&ucurl;" \
             "&Ucurl;&udotbl;&Udotbl;&ubrevinvbl;&udot;&Udot;&uuml;&Uuml;" \
             "&uacute;&Uacute;&udblac;&Udblac;&udotacute;&Udotacute;&ugrave;" \
             "&Ugrave;&uvertline;&Uvertline;&ucirc;&Ucirc;&uumlcirc;" \
             "&Uumlcirc;&ucar;&Ucar;&uring;&Uring;&uhook;&Uhook;&ucurlbar;" \
             "&ubreve;&Ubreve;&umacr;&Umacr;&umacrbreve;&Umacrbreve;" \
             "&umacracute;&Umacracute;&uumlmacr;&Uumlmacr;&uasup;&uesup;" \
             "&Uesup;&uisup;&uosup;&Uosup;&uvsup;&uwsup;&venl;&vscap;&vbar;" \
             "&vslash;&vdiagstrok;&Vdiagstrok;&Vslstrok;&vdotbl;&Vdotbl;" \
             "&vdot;&Vdot;&vuml;&Vuml;&vacute;&Vacute;&vdblac;&Vdblac;" \
             "&vcirc;&Vcirc;&vring;&vmacr;&Vmacr;&Vovlhigh;&wynn;&WYNN;" \
             "&vins;&Vins;&vinsdotbl;&Vinsdotbl;&vinsdot;&Vinsdot;" \
             "&vinsacute;&Vinsacute;&vwelsh;&Vwelsh;&wenl;&wscap;&wdotbl;" \
             "&Wdotbl;&wdot;&Wdot;&wuml;&Wuml;&wacute;&Wacute;&wdblac;" \
             "&Wdblac;&wgrave;&Wgrave;&wcirc;&Wcirc;&wring;&wmacr;&Wmacr;" \
             "&wasup;&wesup;&Wesup;&wisup;&wosup;&wusup;&wvsup;&xenl;&xscap;" \
             "&xmod;&xslashula;&xslashlra;&Xovlhigh;&xldes;&yenl;&yscap;" \
             "&ybar;&ycurl;&Ycurl;&ydotbl;&Ydotbl;&ydot;&Ydot;&yuml;&Yuml;" \
             "&yacute;&Yacute;&ydblac;&Ydblac;&ydotacute;&Ydotacute;&ygrave;" \
             "&Ygrave;&ycirc;&Ycirc;&yring;&yhook;&Yhook;&ybreve;&Ybreve;" \
             "&ymacr;&Ymacr;&ymacrbreve;&Ymacrbreve;&ymacracute;&Ymacracute;" \
             "&yylig;&YYlig;&yyliguml;&YYliguml;&yyligdblac;&YYligdblac;" \
             "&yesup;&yrgmainstrok;&yloop;&Yloop;&zenl;&zscap;&zstrok;" \
             "&Zstrok;&zdotbl;&Zdotbl;&zdot;&Zdot;&zvisigot;&Zvisigot;&ezh;" \
             "&EZH;&yogh;&YOGH;&thorn;&THORN;&thornenl;&thornscap;&thornbar;" \
             "&THORNbar;&thornovlmed;&thornbarslash;&THORNbarslash;" \
             "&thornbardes;&THORNbardes;&thorndotbl;&THORNdotbl;&thornacute;" \
             "&thornslonglig;&thornslongligbar;&thornrarmlig;&frac14;" \
             "&frac12;&frac34;&sup0;&sup1;&sup2;&sup3;&sup4;&sup5;&sup6;" \
             "&sup7;&sup8;&sup9;&sub0;&sub1;&sub2;&sub3;&sub4;&sub5;&sub6;" \
             "&sub7;&sub8;&sub9;&romnumCDlig;&romnumDDlig;&romnumDDdbllig;" \
             "&romnumCrev;&romnumCrevovl;&Imod;&Vmod;&Xmod;&asup;&aeligsup;" \
             "&anligsup;&anscapligsup;&aoligsup;&arligsup;&arscapligsup;" \
             "&avligsup;&bsup;&bscapsup;&csup;&ccedilsup;&dsup;&drotsup;" \
             "&ethsup;&dscapsup;&esup;&eogonsup;&emacrsup;&fsup;&gsup;" \
             "&gscapsup;&hsup;&isup;&inodotsup;&jsup;&jnodotsup;&ksup;" \
             "&kscapsup;&lsup;&lscapsup;&msup;&mscapsup;&nsup;&nscapsup;" \
             "&osup;&omacrsup;&oslashsup;&oogonsup;&orrotsup;&orumsup;&psup;" \
             "&qsup;&rsup;&rrotsup;&rumsup;&rscapsup;&ssup;&slongsup;&tsup;" \
             "&trotsup;&tscapsup;&usup;&vsup;&wsup;&xsup;&ysup;&zsup;" \
             "&thornsup;&combgrave;&combacute;&combcirc;&combcircdbl;" \
             "&combtilde;&combmacr;&combbreve;&combdot;&combuml;&combhook;" \
             "&combring;&combdblac;&combsgvertl;&combdbvertl;&combdotbl;" \
             "&combced;&dblbarbl;&dblovl;&combogon;&combastbl;" \
             "&combdblbrevebl;&combtripbrevebl;&combcurl;&combcurlhigh;" \
             "&combdothigh;&combcurlbar;&bar;&macrhigh;&macrmed;&ovlhigh;" \
             "&ovlmed;&barbl;&baracr;&arbar;&combcomma;&combtildevert;&er;" \
             "&erang;&ercurl;&ersub;&ra;&rabar;&urrot;&urlemn;&ur;&us;" \
             "&combisbelow;&period;&semi;&amp;&Theta;&theta;&obiit;&OBIIT;" \
             "&et;&etslash;&ET;&ETslash;&apomod;&esse;&est;&condes;&CONdes;" \
             "&condot;&CONdot;&usbase;&USbase;&usmod;&rum;&RUM;&de;&is;&IS;" \
             "&sstrok;&etfin;&ETfin;&sem;&fMedrun;&mMedrun;&lbbar;&circ;" \
             "&acute;&grave;&uml;&tld;&macr;&breve;&dot;&ring;&cedil;&ogon;" \
             "&tilde;&dblac;&verbarup;&middot;&hyphpoint;&sgldr;&dblldr;" \
             "&hellip;&colon;&comma;&tridotright;&tridotupw;&tridotdw;" \
             "&quaddot;&lozengedot;&midring;&verbar;&brvbar;&Verbar;&sol;" \
             "&fracsol;&dblsol;&bsol;&luslst;&ruslst;&rlslst;&llslst;" \
             "&lowbar;&hyphen;&dash;&nbhy;&dbloblhyph;&numdash;&ndash;" \
             "&mdash;&horbar;&excl;&iexcl;&quest;&iquest;&ramus;&lpar;&rpar;" \
             "&lUbrack;&rUbrack;&ldblpar;&rdblpar;&lsqb;&rsqb;&lcub;&rcub;" \
             "&lsqbqu;&rsqbqu;&lwhsqb;&rwhsqb;&verbarql;&verbarqr;&luhsqb;" \
             "&ruhsqb;&llhsqb;&rlhsqb;&apos;&prime;&quot;&Prime;&lsquo;" \
             "&rsquo;&lsquolow;&rsquorev;&ldquo;&rdquo;&ldquolow;&rdquorev;" \
             "&lsaquo;&laquo;&lt;&langb;&rsaquo;&gt;&raquo;&rangb;&hidot;" \
             "&posit;&ductsimpl;&punctvers;&punctposit;&colmidcomposit;" \
             "&bidotscomposit;&tridotscomposit;&punctelev;&punctelevdiag;" \
             "&punctelevhiback;&punctelevhack;&punctflex;&punctexclam;" \
             "&punctinter;&punctintertilde;&punctinterlemn;&punctpercont;" \
             "&wavylin;&medcom;&parag;&renvoi;&tridotsdownw;&tridotsupw;" \
             "&quaddots;&fivedots;&virgsusp;&virgmin;&dipledot;&sp;&nbsp;" \
             "&nnbsp;&enqd;&emqd;&ensp;&emsp;&emsp13;&emsp14;&emsp16;&numsp;" \
             "&puncsp;&thinsp;&hairsp;&zerosp;&del;&shy;&num;&sect;&ast;" \
             "&triast;&commat;&copy;&reg;&not;&logand;&para;&revpara;&cross;" \
             "&dagger;&Dagger;&refmark;&dotcross;&hedera;&hederarot;&dollar;" \
             "&cent;&pound;&curren;&yen;&pennygerm;&scruple;&romaslibr;" \
             "&romXbar;&romscapxbar;&romscapybar;&romscapdslash;&drotbar;" \
             "&ecu;&florloop;&grosch;&libradut;&librafren;&libraital;" \
             "&libraflem;&liranuov;&lirasterl;&markold;&markflour;&msign;" \
             "&msignflour;&penningar;&reichtalold;&schillgerm;" \
             "&schillgermscript;&scudi;&ounce;&sestert;&romas;&romunc;" \
             "&romsemunc;&romsext;&romdimsext;&romsiliq;&romquin;&romdupond;" \
             "&plus;&minus;&plusmn;&times;&divide;&equals;&infin;&notequals;" \
             "&percnt;&permil;&deg;&smallzero;&micro;&dram;&obol;&sextans;" \
             "&ouncescript;&arrsgllw;&arrsglupw;&arrsglrw;&arrsgldw;" \
             "&squareblsm;&squarewhsm;&bull;&circledot;&tribull;&trirightwh;" \
             "&trileftwh;&metrshort;&metrshortlong;&metrlongshort;" \
             "&metrdblshortlong;&metranc;&metrancACUTE;&metrancdblac;" \
             "&metrancgrave;&metrancdblgrave;&metrbreve;&metrbreveacute;" \
             "&metrbrevedblac;&metrbrevegrave;&metrbrevedblgrave;&metrmacr;" \
             "&metrmacracute;&metrmacrdblac;&metrmacrgrave;" \
             "&metrmacrdblgrave;&metrmacrbreve;&metrbrevemacr;" \
             "&metrmacrbreveacute;&metrmacrbrevegrave;&metrdblbrevemacr;" \
             "&metrdblbrevemacracute;&metrdblbrevemacrdblac;&metrpause;"

MUFI3_VALS = "ᴀªąĄạẠȧȦäÄáÁàÀâÂãÃåÅảẢăĂāĀắẮꜳꜲ" \
             "æÆᴁǽǼǣǢ" \
             "ꜵꜴꜷꜶꜹꜸꜻꜺꜽꜼ" \
             "ʙḅḄḃḂƀᴄçÇċĊćĆ" \
             "ↃↄᴅđĐꝱɖḍḌḋḊðÐᴆꝹꝺẟᴇęĘẹẸė" \
             "ĖëËéÉèÈêÊĕĔēĒḗḖəꜰḟḞ" \
             "ﬀﬁﬂﬃﬄⅎℲꟻꝼꝻɢǥǤġĠǴǵ" \
             "ᵹꝽꝿꝾɡʜɦħḥḤḣḢƕǶⱶⱵɪıİɨįĮịỊïÏ" \
             "íÍìÌîÎỉỈĭĬīĪĳĲꟾᴊȷɟɉɈᴋƙ" \
             "ꝁꝀꝃꝂꝅꝄḳḲḱḰʟƚłŁꝉꝈꝲḷḶĺĹꝇꝆỻỺꞁꞀᴍꝳṃṂṁ" \
             "ṀḿḾꟽꟿɴƞɲꝴṅṄńŃṇṆñÑŋŊ" \
             "ᴏºǫǪøØọỌȯȮǭǬöÖóÓǿǾőŐ" \
             "òÒôÔǒǑõÕỏỎŏŎōŌṓṒȫȪœŒɶꝌꝍ" \
             "ꝏꝎɔᴘꝑꝐꝓꝒꝕꝔṗṖṕṔꟼꝙꝘꝗꝖ" \
             "ʀƦɼꝵꝶ℞℟ṛṚṙṘŕŔꝛꝚꞃꞂꜱṡṠśŚṣṢßẞ" \
             "ﬆﬅſẜẝꞅꞄᴛꝷṭṬṫṪ" \
             "ꞇꞆᴜʉųŲụỤüÜúÚűŰùÙûÛǔǓůŮủỦŭŬūŪǖǕ" \
             "ᴠꝟꝞ℣ṿṾƿǷꝩꝨỽỼᴡẉẈẇẆẅẄẃẂẁẀŵŴẘ" \
             "ˣʏỵỴẏẎÿŸýÝỳỲŷŶẙỷỶȳȲꝡꝠỿỾᴢ" \
             "ƶƵẓẒżŻꝣꝢʒƷȝȜþÞꝥꝤꝧꝦ¼½¾⁰¹²³⁴⁵⁶⁷⁸⁹₀₁₂₃₄₅₆₇₈₉ↀↁↂↃ" \
             "ᴵͣᷔᷕᷖͨᷗͩᷘᷙͤᷚᷛͪͥᷜᷝᷞͫᷟᷠᷡͦͬᷣᷢᷤᷥͭͧͮͯᷦ" \
             "̧̨̣̳͙̀́̂̃̄̆̇̈̉̊̋̍̎̿͜᷍᷎̅̶̲̾͛̕᷏ᷓ᷐᷑᷒.;&ΘθꝋꝊ⁊ʼ≈∻ꝯ" \
             "ꝮꜿꜾꝰꝝꝜꝭꝬꝸꝫꝪᚠᛘ℔^´`¨~¯˘˙˚¸˛˜˝ˈ·‧․‥…:,჻∴∵∷⁘|¦‖/⁄⫽\\⸌⸍⸜⸝_" \
             "-‐‑⸗‒–—―!¡?¿()⸦⸧⸨⸩[]{}⁅⁆⟦⟧⸡⸠⸢⸣⸤⸥'′\"″‘’‚‛“”„‟‹«<⟨›>»⟩" \
             "⸮⸪⸫⸬⸭⋗              ​­#§*⁂@©®¬∧¶" \
             "⁋✝†‡※⁜❦❧$¢£¤¥₰℈℥" \
             "+−±×÷=∞≠%‰°µ←↑→↓▪▫•◌‣▹◃⏑⏒⏓⏔"

MUFI4 = {'&aenl;': '\ueee0', '&ascap;': 'ᴀ', '&ordf;': 'ª', '&aogon;': 'ą',
         '&Aogon;': 'Ą', '&acurl;': '\ue433', '&Acurl;': '\ue033',
         '&adotbl;': 'ạ', '&Adotbl;': 'Ạ', '&adot;': 'ȧ', '&Adot;': 'Ȧ',
         '&auml;': 'ä', '&Auml;': 'Ä', '&adiaguml;': '\ue8d5',
         '&adotbluml;': '\ue41d', '&aacute;': 'á', '&Aacute;': 'Á',
         '&aenlacute;': '\ueaf0', '&aogonacute;': '\ue404',
         '&Aogonacute;': '\ue004', '&adblac;': '\ue425', '&Adblac;': '\ue025',
         '&adotacute;': '\uebf5', '&Adotacute;': '\uebf4', '&agrave;': 'à',
         '&Agrave;': 'À', '&acirc;': 'â', '&Acirc;': 'Â',
         '&aumlcirc;': '\ue41a', '&aringcirc;': '\ue41f', '&atilde;': 'ã',
         '&Atilde;': 'Ã', '&aring;': 'å', '&Aring;': 'Å', '&ahook;': 'ả',
         '&Ahook;': 'Ả', '&abreve;': 'ă', '&Abreve;': 'Ă', '&amacr;': 'ā',
         '&Amacr;': 'Ā', '&amacrbreve;': '\ue410', '&Amacrbreve;': '\ue010',
         '&abreveacute;': 'ắ', '&Abreveacute;': 'Ắ', '&amacracute;': '\ue40a',
         '&Amacracute;': '\ue00a', '&aalig;': 'ꜳ', '&aacloselig;': '\uefa0',
         '&AAlig;': 'Ꜳ', '&aaligenl;': '\uefdf', '&aaligdotbl;': '\ueff3',
         '&AAligdotbl;': '\ueff2', '&aaligdot;': '\uefef',
         '&AAligdot;': '\uefee', '&aaliguml;': '\uefff',
         '&AAliguml;': '\ueffe', '&aaligacute;': '\uefe1',
         '&AAligacute;': '\uefe0', '&aaligdblac;': '\uefeb',
         '&AAligdblac;': '\uefea', '&aelig;': 'æ', '&AElig;': 'Æ',
         '&aeligenl;': '\ueaf1', '&aeligscap;': 'ᴁ', '&aeligred;': '\uf204',
         '&aeligcurl;': '\uebeb', '&AEligcurl;': '\uebea',
         '&aeligogon;': '\ue440', '&AEligogon;': '\ue040',
         '&aeligdotbl;': '\ue436', '&AEligdotbl;': '\ue036',
         '&aeligdot;': '\ue443', '&AEligdot;': '\ue043',
         '&aeliguml;': '\ue442', '&AEliguml;': '\ue042', '&aeligacute;': 'ǽ',
         '&AEligacute;': 'Ǽ', '&aeligogonacute;': '\ue8d3',
         '&aeligdblac;': '\ue441', '&AEligdblac;': '\ue041',
         '&aeligring;': '\ue8d1', '&aeligbreve;': '\ue43f',
         '&AEligbreve;': '\ue03f', '&aeligmacr;': 'ǣ', '&AEligmacr;': 'Ǣ',
         '&aeligmacrbreve;': '\ue43d', '&AEligmacrbreve;': '\ue03d',
         '&aeligmacracute;': '\ue43a', '&AEligmacracute;': '\ue03a',
         '&aeligdotacute;': '\uefdb', '&AEligdotacute;': '\uefdc',
         '&aflig;': '\uefa3', '&afinslig;': '\uefa4', '&aglig;': '\uefa5',
         '&allig;': '\uefa6', '&anlig;': '\uefa7', '&anscaplig;': '\uefa8',
         '&aolig;': 'ꜵ', '&AOlig;': 'Ꜵ', '&aoligenl;': '\uefde',
         '&aenlosmalllig;': '\ueaf2', '&aoligred;': '\uf206',
         '&AOligred;': '\uf205', '&aoligdotbl;': '\ueff5',
         '&AOligdotbl;': '\ueff4', '&aoligacute;': '\uefe3',
         '&AOligacute;': '\uefe2', '&aoligdblac;': '\uebc1',
         '&AOligdblac;': '\uebc0', '&aplig;': '\uefa9',
         '&arlig;': '\uefaa', '&arscaplig;': '\uefab', '&aulig;': 'ꜷ',
         '&AUlig;': 'Ꜷ', '&auligdotbl;': '\ueff7', '&AUligdotbl;': '\ueff6',
         '&auligacute;': '\uefe5', '&AUligacute;': '\uefe4', '&avlig;': 'ꜹ',
         '&AVlig;': 'Ꜹ', '&avligslash;': 'ꜻ', '&AVligslash;': 'Ꜻ',
         '&avligslashacute;': '\uebb1', '&AVligslashacute;': '\uebb0',
         '&avligogon;': '\uebf1', '&AVligogon;': '\uebf0',
         '&avligdotbl;': '\ueff9', '&AVligdotbl;': '\ueff8',
         '&avligacute;': '\uefe7', '&AVligacute;': '\uefe6',
         '&avligdblac;': '\uebc3', '&AVligdblac;': '\uebc2',
         '&aylig;': 'ꜽ', '&AYlig;': 'Ꜽ', '&ayligdotbl;': '\ueffb',
         '&AYligdotbl;': '\ueffa', '&ayligdot;': '\ueff1',
         '&AYligdot;': '\ueff0', '&athornlig;': '\uefac', '&aesup;': '\ue42c',
         '&Aesup;': '\ue02c', '&iesup;': '\ue54a', '&aosup;': '\ue42d',
         '&ausup;': '\ue8e1', '&avsup;': '\ue42e', '&aunc;': '\uf214',
         '&aopen;': '\uf202', '&ains;': '\uf200', '&Ains;': '\uf201',
         '&aneckless;': '\uf215', '&anecklesselig;': '\uefa1',
         '&AnecklessElig;': '\uefae', '&anecklessvlig;': '\uefa2',
         '&aclose;': '\uf203', '&Asqu;': '\uf13a', '&benl;': '\ueee1',
         '&bscap;': 'ʙ', '&bscapdot;': '\uebd0', '&bscapdotbl;': '\uef25',
         '&bdotbl;': 'ḅ', '&Bdotbl;': 'Ḅ', '&bdot;': 'ḃ', '&Bdot;': 'Ḃ',
         '&bacute;': '\ue444', '&Bacute;': '\ue044', '&bstrok;': 'ƀ',
         '&bovlmed;': '\ue44d', '&bblig;': '\ueec2', '&bglig;': '\ueec3',
         '&cenl;': '\ueee2', '&cscap;': 'ᴄ', '&ccedil;': 'ç', '&Ccedil;': 'Ç',
         '&cogon;': '\ue476', '&Cogon;': '\ue076', '&cdotbl;': '\ue466',
         '&Cdotbl;': '\ue066', '&cdot;': 'ċ', '&Cdot;': 'Ċ', '&cacute;': 'ć',
         '&Cacute;': 'Ć', '&Covlhigh;': '\uf7b5', '&chlig;': '\uf1bb',
         '&cklig;': '\ueec4', '&ctlig;': '\ueec5', '&Csqu;': '\uf106',
         '&ccurl;': '\uf198', '&CONbase;': 'Ↄ', '&conbase;': 'ↄ',
         '&denl;': '\ueee3', '&dscap;': 'ᴅ', '&dstrok;': 'đ', '&Dstrok;': 'Đ',
         '&dovlmed;': '\ue491', '&dtailstrok;': 'ꝱ', '&dtail;': 'ɖ',
         '&dscapdot;': '\uebd2', '&ddotbl;': 'ḍ', '&Ddotbl;': 'Ḍ',
         '&dscapdotbl;': '\uef26', '&ddot;': 'ḋ', '&Ddot;': 'Ḋ',
         '&dacute;': '\ue477', '&Dacute;': '\ue077', '&eth;': 'ð',
         '&ETH;': 'Ð', '&ethenl;': '\ueee5', '&ethscap;': 'ᴆ',
         '&ethdotbl;': '\ue48f', '&ETHdotbl;': '\ue08f',
         '&Dovlhigh;': '\uf7b6', '&drotdrotlig;': '\ueec6', '&Drot;': 'Ꝺ',
         '&drot;': 'ꝺ', '&drotdot;': '\uebd1', '&drotacute;': '\uebb2',
         '&drotenl;': '\ueee4', '&dscript;': 'ẟ', '&dcurl;': '\uf193',
         '&eenl;': '\ueee6', '&escap;': 'ᴇ', '&eogon;': 'ę', '&Eogon;': 'Ę',
         '&ecurl;': '\ue4e9', '&Ecurl;': '\ue0e9', '&eogoncurl;': '\uebf3',
         '&Eogoncurl;': '\uebf2', '&edotbl;': 'ẹ', '&Edotbl;': 'Ẹ',
         '&eogondot;': '\ue4eb', '&Eogondot;': '\ue0eb',
         '&eogondotbl;': '\ue4e8', '&Eogondotbl;': '\ue0e8',
         '&eogonenl;': '\ueaf3', '&edot;': 'ė', '&Edot;': 'Ė', '&euml;': 'ë',
         '&Euml;': 'Ë', '&eumlmacr;': '\ue4cd', '&eacute;': 'é',
         '&Eacute;': 'É', '&eogonacute;': '\ue499', '&Eogonacute;': '\ue099',
         '&edotblacute;': '\ue498', '&edblac;': '\ue4d1', '&Edblac;': '\ue0d1',
         '&edotacute;': '\ue4c8', '&Edotacute;': '\ue0c8',
         '&eogondotacute;': '\ue4ec', '&Eogondotacute;': '\ue0ec',
         '&eogondblac;': '\ue4ea', '&Eogondblac;': '\ue0ea', '&egrave;': 'è',
         '&Egrave;': 'È', '&ecirc;': 'ê', '&Ecirc;': 'Ê',
         '&eogoncirc;': '\ue49f', '&ering;': '\ue4cf', '&ebreve;': 'ĕ',
         '&Ebreve;': 'Ĕ', '&emacr;': 'ē', '&Emacr;': 'Ē',
         '&eogonmacr;': '\ue4bc', '&Eogonmacr;': '\ue0bc',
         '&emacrbreve;': '\ue4b7', '&Emacrbreve;': '\ue0b7',
         '&emacracute;': 'ḗ', '&Emacracute;': 'Ḗ', '&eylig;': '\ueec7',
         '&eacombcirc;': '\uebbd', '&eucombcirc;': '\uebbe',
         '&easup;': '\ue4e1', '&Easup;': '\ue0e1', '&eesup;': '\ue8e2',
         '&eisup;': '\ue4e2', '&eosup;': '\ue8e3', '&evsup;': '\ue4e3',
         '&schwa;': 'ə', '&Eunc;': '\uf10a', '&Euncclose;': '\uf217',
         '&eunc;': '\uf218', '&eext;': '\uf219', '&etall;': '\uf21a',
         '&fenl;': '\ueee7', '&fscap;': 'ꜰ', '&fdotbl;': '\ue4ee',
         '&Fdotbl;': '\ue0ee', '&fdot;': 'ḟ', '&Fdot;': 'Ḟ',
         '&fscapdot;': '\uebd7', '&facute;': '\ue4f0', '&Facute;': '\ue0f0',
         '&faumllig;': '\ueec8', '&fflig;': 'ﬀ', '&filig;': 'ﬁ',
         '&fjlig;': '\ueec9', '&foumllig;': '\uf1bc', '&fllig;': 'ﬂ',
         '&frlig;': '\ueeca', '&ftlig;': '\ueecb', '&fuumllig;': '\ueecc',
         '&fylig;': '\ueecd', '&ffilig;': 'ﬃ', '&ffllig;': 'ﬄ',
         '&fftlig;': '\ueece', '&ffylig;': '\ueecf', '&ftylig;': '\ueed0',
         '&fturn;': 'ⅎ', '&Fturn;': 'Ⅎ', '&Frev;': 'ꟻ', '&fins;': 'ꝼ',
         '&Fins;': 'Ꝼ', '&finsenl;': '\ueeff', '&finsdot;': '\uebd4',
         '&Finsdot;': '\uebd3', '&finsdothook;': '\uf21c',
         '&finssemiclose;': '\uf21b', '&finssemiclosedot;': '\uebd5',
         '&finsclose;': '\uf207', '&finsclosedot;': '\uebd6',
         '&finsdotbl;': '\ue7e5', '&Finsdotbl;': '\ue3e5',
         '&finsacute;': '\uebb4', '&Finsacute;': '\uebb3', '&fcurl;': '\uf194',
         '&genl;': '\ueee8', '&gscap;': 'ɢ', '&gstrok;': 'ǥ', '&Gstrok;': 'Ǥ',
         '&gdotbl;': '\ue501', '&Gdotbl;': '\ue101', '&gscapdotbl;': '\uef27',
         '&gdot;': 'ġ', '&Gdot;': 'Ġ', '&gscapdot;': '\uef20', '&Gacute;': 'Ǵ',
         '&gacute;': 'ǵ', '&gglig;': '\ueed1', '&gdlig;': '\ueed2',
         '&gdrotlig;': '\ueed3', '&gethlig;': '\ueed4', '&golig;': '\ueede',
         '&gplig;': '\uead2', '&grlig;': '\uead0', '&gins;': 'ᵹ',
         '&Gins;': 'Ᵹ', '&ginsturn;': 'ꝿ', '&Ginsturn;': 'Ꝿ',
         '&Gsqu;': '\uf10e', '&gdivloop;': '\uf21d', '&glglowloop;': '\uf21e',
         '&gsmlowloop;': '\uf21f', '&gopen;': 'ɡ', '&gcurl;': '\uf196',
         '&henl;': '\ueee9', '&hscap;': 'ʜ', '&hhook;': 'ɦ', '&hstrok;': 'ħ',
         '&hovlmed;': '\ue517', '&hdotbl;': 'ḥ', '&Hdotbl;': 'Ḥ',
         '&Hdot;': 'ḣ', '&hdot;': 'Ḣ', '&hscapdot;': '\uebda',
         '&hacute;': '\ue516', '&Hacute;': '\ue116', '&hwair;': 'ƕ',
         '&HWAIR;': 'Ƕ', '&hslonglig;': '\uebad', '&hslongligbar;': '\ue7c7',
         '&hrarmlig;': '\ue8c3', '&Hrarmlig;': '\ue8c2', '&hhalf;': 'ⱶ',
         '&Hhalf;': 'Ⱶ', '&Hunc;': '\uf110', '&hrdes;': '\uf23a',
         '&ienl;': '\ueeea', '&iscap;': 'ɪ', '&inodot;': 'ı',
         '&inodotenl;': '\ueefd', '&Idot;': 'İ', '&istrok;': 'ɨ',
         '&idblstrok;': '\ue8a1', '&iogon;': 'į', '&inodotogon;': '\ue8dd',
         '&Iogon;': 'Į', '&icurl;': '\ue52a', '&Icurl;': '\ue12a',
         '&idotbl;': 'ị', '&Idotbl;': 'Ị', '&ibrevinvbl;': '\ue548',
         '&iuml;': 'ï', '&Iuml;': 'Ï', '&iacute;': 'í', '&Iacute;': 'Í',
         '&idblac;': '\ue543', '&Idblac;': '\ue143', '&idotacute;': '\uebf7',
         '&Idotacute;': '\uebf6', '&igrave;': 'ì', '&Igrave;': 'Ì',
         '&icirc;': 'î', '&Icirc;': 'Î', '&ihook;': 'ỉ', '&Ihook;': 'Ỉ',
         '&ibreve;': 'ĭ', '&Ibreve;': 'Ĭ', '&imacr;': 'ī', '&Imacr;': 'Ī',
         '&iovlmed;': '\ue550', '&Iovlhigh;': '\ue150',
         '&imacrbreve;': '\ue537', '&Imacrbreve;': '\ue137',
         '&imacracute;': '\ue535', '&Imacracute;': '\ue135', '&ijlig;': 'ĳ',
         '&IJlig;': 'Ĳ', '&iasup;': '\ue8e4', '&iosup;': '\ue8e5',
         '&iusup;': '\ue8e6', '&ivsup;': '\ue54b', '&ilong;': '\uf220',
         '&Ilong;': 'ꟾ', '&jenl;': '\ueeeb', '&jscap;': 'ᴊ', '&jnodot;': 'ȷ',
         '&jnodotenl;': '\ueefe', '&Jdot;': '\ue15c', '&jnodotstrok;': 'ɟ',
         '&jbar;': 'ɉ', '&jdblstrok;': '\ue8a2', '&Jbar;': 'Ɉ',
         '&jcurl;': '\ue563', '&Jcurl;': '\ue163', '&juml;': '\uebe3',
         '&Juml;': '\uebe2', '&jdotbl;': '\ue551', '&Jdotbl;': '\ue151',
         '&jacute;': '\ue553', '&Jacute;': '\ue153', '&jdblac;': '\ue562',
         '&Jdblac;': '\ue162', '&jmacrmed;': '\ue554', '&jovlmed;': '\ue552',
         '&Jmacrhigh;': '\ue154', '&Jovlhigh;': '\ue152', '&jesup;': '\ue8e7',
         '&kenl;': '\ueeec', '&kscap;': 'ᴋ', '&khook;': 'ƙ', '&kbar;': 'ꝁ',
         '&Kbar;': 'Ꝁ', '&kovlmed;': '\ue7c3', '&kstrleg;': 'ꝃ',
         '&Kstrleg;': 'Ꝃ', '&kstrascleg;': 'ꝅ', '&Kstrascleg;': 'Ꝅ',
         '&kdot;': '\ue568', '&Kdot;': '\ue168', '&kscapdot;': '\uebdb',
         '&kdotbl;': 'ḳ', '&Kdotbl;': 'Ḳ', '&kacute;': 'ḱ', '&Kacute;': 'Ḱ',
         '&kslonglig;': '\uebae', '&kslongligbar;': '\ue7c8',
         '&krarmlig;': '\ue8c5', '&kunc;': '\uf208', '&ksemiclose;': '\uf221',
         '&kclose;': '\uf209', '&kcurl;': '\uf195', '&lenl;': '\ueeed',
         '&lscap;': 'ʟ', '&lbar;': 'ƚ', '&lstrok;': 'ł', '&Lstrok;': 'Ł',
         '&lhighstrok;': 'ꝉ', '&Lhighstrok;': 'Ꝉ', '&lovlmed;': '\ue5b1',
         '&ltailstrok;': 'ꝲ', '&ldotbl;': 'ḷ', '&Ldotbl;': 'Ḷ',
         '&lscapdotbl;': '\uef28', '&ldot;': '\ue59e', '&Ldot;': '\ue19e',
         '&lscapdot;': '\uebdc', '&lacute;': 'ĺ', '&Lacute;': 'Ĺ',
         '&lringbl;': '\ue5a4', '&lmacrhigh;': '\ue596',
         '&lovlhigh;': '\ue58c', '&Lovlhigh;': '\uf7b4', '&lbrk;': 'ꝇ',
         '&Lbrk;': 'Ꝇ', '&llwelsh;': 'ỻ', '&LLwelsh;': 'Ỻ',
         '&lllig;': '\uf4f9', '&ldes;': '\uf222', '&lturn;': 'ꞁ',
         '&Lturn;': 'Ꞁ', '&menl;': '\ueeee', '&mscap;': 'ᴍ',
         '&mtailstrok;': 'ꝳ', '&mdotbl;': 'ṃ', '&Mdotbl;': 'Ṃ',
         '&mscapdotbl;': '\uef29', '&mdot;': 'ṁ', '&Mdot;': 'Ṁ',
         '&mscapdot;': '\uebdd', '&macute;': 'ḿ', '&Macute;': 'Ḿ',
         '&mringbl;': '\ue5c5', '&mmacrmed;': '\ue5b8',
         '&Mmacrhigh;': '\ue1b8', '&movlmed;': '\ue5d2',
         '&Movlhigh;': '\ue1d2', '&mesup;': '\ue8e8', '&Minv;': 'ꟽ',
         '&mturn;': 'ɯ', '&Mturn;': 'Ɯ', '&munc;': '\uf23c',
         '&mmedunc;': '\uf225', '&Munc;': '\uf11a', '&mrdes;': '\uf223',
         '&muncdes;': '\uf23d', '&mmeduncdes;': '\uf226',
         '&Muncdes;': '\uf224', '&muncacute;': '\uf23e',
         '&mmeduncacute;': '\uebb6', '&Muncacute;': '\uebb5', '&M5leg;': 'ꟿ',
         '&nenl;': '\ueeef', '&nscap;': 'ɴ', '&nscapldes;': '\uf22b',
         '&nlrleg;': 'ƞ', '&nlfhook;': 'ɲ', '&nbar;': '\ue7b2',
         '&ntailstrok;': 'ꝴ', '&ndot;': 'ṅ', '&Ndot;': 'Ṅ',
         '&nscapdot;': '\uef21', '&nacute;': 'ń', '&Nacute;': 'Ń',
         '&ndotbl;': 'ṇ', '&Ndotbl;': 'Ṇ', '&nscapdotbl;': '\uef2a',
         '&ncirc;': '\ue5d7', '&ntilde;': 'ñ', '&Ntilde;': 'Ñ',
         '&nringbl;': '\ue5ee', '&nmacrmed;': '\ue5dc',
         '&Nmacrhigh;': '\ue1dc', '&eng;': 'ŋ', '&ENG;': 'Ŋ',
         '&nscapslonglig;': '\ueed5', '&nrdes;': '\uf228', '&Nrdes;': '\uf229',
         '&nscaprdes;': '\uf22a', '&nflour;': '\uf19a', '&oenl;': '\ueef0',
         '&oscap;': 'ᴏ', '&ordm;': 'º', '&oogon;': 'ǫ', '&Oogon;': 'Ǫ',
         '&ocurl;': '\ue7d3', '&Ocurl;': '\ue3d3', '&oogoncurl;': '\ue64f',
         '&Oogoncurl;': '\ue24f', '&ocurlacute;': '\uebb8',
         '&Ocurlacute;': '\uebb7', '&oslash;': 'ø', '&Oslash;': 'Ø',
         '&oslashcurl;': '\ue7d4', '&Oslashcurl;': '\ue3d4',
         '&oslashogon;': '\ue655', '&Oslashogon;': '\ue255', '&odotbl;': 'ọ',
         '&Odotbl;': 'Ọ', '&oslashdotbl;': '\uebe1', '&Oslashdotbl;': '\uebe0',
         '&odot;': 'ȯ', '&Odot;': 'Ȯ', '&oogondot;': '\uebdf',
         '&Oogondot;': '\uebde', '&oogonmacr;': 'ǭ', '&Oogonmacr;': 'Ǭ',
         '&oslashdot;': '\uebce', '&Oslashdot;': '\uebcd',
         '&oogondotbl;': '\ue608', '&Oogondotbl;': '\ue208', '&ouml;': 'ö',
         '&Ouml;': 'Ö', '&odiaguml;': '\ue8d7', '&oumlacute;': '\ue62c',
         '&oacute;': 'ó', '&Oacute;': 'Ó', '&oslashacute;': 'ǿ',
         '&Oslashacute;': 'Ǿ', '&oslashdblac;': '\uebc7',
         '&Oslashdblac;': '\uebc6', '&oogonacute;': '\ue60c',
         '&Oogonacute;': '\ue20c', '&oslashogonacute;': '\ue657',
         '&Oslashogonacute;': '\ue257', '&odblac;': 'ő', '&Odblac;': 'Ő',
         '&odotacute;': '\uebf9', '&Odotacute;': '\uebf8',
         '&oogondotacute;': '\uebfb', '&Oogondotacute;': '\uebfa',
         '&oslashdotacute;': '\uebfd', '&Oslashdotacute;': '\uebfc',
         '&oogondblac;': '\uebc5', '&Oogondblac;': '\uebc4', '&ograve;': 'ò',
         '&Ograve;': 'Ò', '&ocirc;': 'ô', '&Ocirc;': 'Ô',
         '&oumlcirc;': '\ue62d', '&Oumlcirc;': '\ue22d',
         '&oogoncirc;': '\ue60e', '&ocar;': 'ǒ', '&Ocar;': 'Ǒ',
         '&otilde;': 'õ', '&Otilde;': 'Õ', '&oring;': '\ue637', '&ohook;': 'ỏ',
         '&Ohook;': 'Ỏ', '&obreve;': 'ŏ', '&Obreve;': 'Ŏ',
         '&oslashbreve;': '\uebef', '&Oslashbreve;': '\uebee', '&omacr;': 'ō',
         '&Omacr;': 'Ō', '&oslashmacr;': '\ue652', '&Oslashmacr;': '\ue252',
         '&omacrbreve;': '\ue61b', '&Omacrbreve;': '\ue21b',
         '&oslashmacrbreve;': '\ue653', '&Oslashmacrbreve;': '\ue253',
         '&omacracute;': 'ṓ', '&Omacracute;': 'Ṓ',
         '&oslashmacracute;': '\uebed', '&Oslashmacracute;': '\uebec',
         '&oumlmacr;': 'ȫ', '&Oumlmacr;': 'Ȫ', '&oclig;': '\uefad',
         '&oelig;': 'œ', '&OElig;': 'Œ', '&oeligscap;': 'ɶ',
         '&oeligenl;': '\uefdd', '&oeligogon;': '\ue662',
         '&OEligogon;': '\ue262', '&Oloop;': 'Ꝍ', '&oloop;': 'ꝍ',
         '&oeligacute;': '\ue659', '&OEligacute;': '\ue259',
         '&oeligdblac;': '\uebc9', '&OEligdblac;': '\uebc8',
         '&oeligmacr;': '\ue65d', '&OEligmacr;': '\ue25d',
         '&oeligmacrbreve;': '\ue660', '&OEligmacrbreve;': '\ue260',
         '&oolig;': 'ꝏ', '&OOlig;': 'Ꝏ', '&ooliguml;': '\uebe5',
         '&OOliguml;': '\uebe4', '&ooligacute;': '\uefe9',
         '&OOligacute;': '\uefe8', '&ooligdblac;': '\uefed',
         '&OOligdblac;': '\uefec', '&ooligdotbl;': '\ueffd',
         '&OOligdotbl;': '\ueffc', '&orrotlig;': '\ue8de', '&oasup;': '\ue643',
         '&oesup;': '\ue644', '&Oesup;': '\ue244', '&oisup;': '\ue645',
         '&oosup;': '\ue8e9', '&ousup;': '\ue646', '&Ousup;': '\ue246',
         '&ovsup;': '\ue647', '&oopen;': 'ɔ', '&oopenmacr;': '\ue7cc',
         '&penl;': '\ueef1', '&pscap;': 'ᴘ', '&pbardes;': 'ꝑ',
         '&Pbardes;': 'Ꝑ', '&pflour;': 'ꝓ', '&Pflour;': 'Ꝓ',
         '&psquirrel;': 'ꝕ', '&Psquirrel;': 'Ꝕ', '&pdotbl;': '\ue66d',
         '&Pdotbl;': '\ue26d', '&pdot;': 'ṗ', '&Pdot;': 'Ṗ',
         '&pscapdot;': '\uebcf', '&pacute;': 'ṕ', '&Pacute;': 'Ṕ',
         '&pdblac;': '\ue668', '&Pdblac;': '\ue268', '&pmacr;': '\ue665',
         '&pplig;': '\ueed6', '&PPlig;': '\ueedd', '&ppflourlig;': '\ueed7',
         '&ppliguml;': '\uebe7', '&PPliguml;': '\uebe6', '&Prev;': 'ꟼ',
         '&qenl;': '\ueef2', '&qscap;': '\uef0c', '&qslstrok;': 'ꝙ',
         '&Qslstrok;': 'Ꝙ', '&qbardes;': 'ꝗ', '&Qbardes;': 'Ꝗ',
         '&qbardestilde;': '\ue68b', '&q2app;': '\ue8b3', '&q3app;': '\ue8bf',
         '&qcentrslstrok;': '\ue8b4', '&qdotbl;': '\ue688',
         '&Qdotbl;': '\ue288', '&qdot;': '\ue682', '&Qdot;': '\ue282',
         '&qmacr;': '\ue681', '&qvinslig;': '\uead1', '&Qstem;': '\uf22c',
         '&renl;': '\ueef3', '&rscap;': 'ʀ', '&YR;': 'Ʀ', '&rdes;': 'ɼ',
         '&rdesstrok;': '\ue7e4', '&rtailstrok;': 'ꝵ', '&rscaptailstrok;': 'ꝶ',
         '&Rtailstrok;': '℞', '&Rslstrok;': '℟', '&rdotbl;': 'ṛ',
         '&Rdotbl;': 'Ṛ', '&rdot;': 'ṙ', '&Rdot;': 'Ṙ', '&rscapdot;': '\uef22',
         '&racute;': 'ŕ', '&Racute;': 'Ŕ', '&rringbl;': '\ue6a3',
         '&rscapdotbl;': '\uef2b', '&resup;': '\ue8ea', '&rrot;': 'ꝛ',
         '&Rrot;': 'Ꝛ', '&rrotdotbl;': '\ue7c1', '&rrotacute;': '\uebb9',
         '&rins;': 'ꞃ', '&Rins;': 'Ꞃ', '&rflour;': '\uf19b',
         '&senl;': '\ueef4', '&sscap;': 'ꜱ', '&sdot;': 'ṡ', '&Sdot;': 'Ṡ',
         '&sscapdot;': '\uef23', '&sacute;': 'ś', '&Sacute;': 'Ś',
         '&sdotbl;': 'ṣ', '&Sdotbl;': 'Ṣ', '&sscapdotbl;': '\uef2c',
         '&szlig;': 'ß', '&SZlig;': 'ẞ', '&slongaumllig;': '\ueba0',
         '&slongchlig;': '\uf4fa', '&slonghlig;': '\ueba1',
         '&slongilig;': '\ueba2', '&slongjlig;': '\uf4fb',
         '&slongklig;': '\uf4fc', '&slongllig;': '\ueba3',
         '&slonglbarlig;': '\ue8df', '&slongoumllig;': '\ueba4',
         '&slongplig;': '\ueba5', '&slongslig;': '\uf4fd',
         '&slongslonglig;': '\ueba6', '&slongslongilig;': '\ueba7',
         '&slongslongklig;': '\uf4fe', '&slongslongllig;': '\ueba8',
         '&slongslongtlig;': '\uf4ff', '&stlig;': 'ﬆ', '&slongtlig;': 'ﬅ',
         '&slongtilig;': '\ueba9', '&slongtrlig;': '\uebaa',
         '&slonguumllig;': '\uebab', '&slongvinslig;': '\uebac',
         '&slongdestlig;': '\ueada', '&slong;': 'ſ', '&slongenl;': '\ueedf',
         '&slongbarslash;': 'ẜ', '&slongbar;': 'ẝ', '&slongovlmed;': '\ue79e',
         '&slongslstrok;': '\ue8b8', '&slongflour;': '\ue8b7',
         '&slongacute;': '\uebaf', '&slongdes;': '\uf127',
         '&slongdotbl;': '\ue7c2', '&Sclose;': '\uf126', '&sclose;': '\uf128',
         '&sins;': 'ꞅ', '&Sins;': 'Ꞅ', '&tenl;': '\ueef5', '&tscap;': 'ᴛ',
         '&ttailstrok;': 'ꝷ', '&togon;': '\ue6ee', '&Togon;': '\ue2ee',
         '&tdotbl;': 'ṭ', '&Tdotbl;': 'Ṭ', '&tdot;': 'ṫ', '&Tdot;': 'Ṫ',
         '&tscapdot;': '\uef24', '&tscapdotbl;': '\uef2d',
         '&tacute;': '\ue6e2', '&Tacute;': '\ue2e2', '&trlig;': '\ueed8',
         '&ttlig;': '\ueed9', '&trottrotlig;': '\ueeda', '&tylig;': '\ueedb',
         '&tzlig;': '\ueedc', '&trot;': 'ꞇ', '&Trot;': 'Ꞇ',
         '&tcurl;': '\uf199', '&uenl;': '\ueef7', '&uscap;': 'ᴜ',
         '&ubar;': 'ʉ', '&uogon;': 'ų', '&Uogon;': 'Ų', '&ucurl;': '\ue731',
         '&Ucurl;': '\ue331', '&udotbl;': 'ụ', '&Udotbl;': 'Ụ',
         '&ubrevinvbl;': '\ue727', '&udot;': '\ue715', '&Udot;': '\ue315',
         '&uuml;': 'ü', '&Uuml;': 'Ü', '&uacute;': 'ú', '&Uacute;': 'Ú',
         '&udblac;': 'ű', '&Udblac;': 'Ű', '&udotacute;': '\uebff',
         '&Udotacute;': '\uebfe', '&ugrave;': 'ù', '&Ugrave;': 'Ù',
         '&uvertline;': '\ue724', '&Uvertline;': '\ue324', '&ucirc;': 'û',
         '&Ucirc;': 'Û', '&uumlcirc;': '\ue717', '&Uumlcirc;': '\ue317',
         '&ucar;': 'ǔ', '&Ucar;': 'Ǔ', '&uring;': 'ů', '&Uring;': 'Ů',
         '&uhook;': 'ủ', '&Uhook;': 'Ủ', '&ucurlbar;': '\uebbf',
         '&ubreve;': 'ŭ', '&Ubreve;': 'Ŭ', '&umacr;': 'ū', '&Umacr;': 'Ū',
         '&umacrbreve;': '\ue70b', '&Umacrbreve;': '\ue30b',
         '&umacracute;': '\ue709', '&Umacracute;': '\ue309', '&uumlmacr;': 'ǖ',
         '&Uumlmacr;': 'Ǖ', '&uelig;': '\ue8c9', '&UElig;': '\ue8c8',
         '&uulig;': '\ue8c7', '&UUlig;': '\ue8c6', '&uuligdblac;': '\uefd8',
         '&UUligdblac;': '\uefd9', '&uasup;': '\ue8eb', '&uesup;': '\ue72b',
         '&Uesup;': '\ue32b', '&uisup;': '\ue72c', '&uosup;': '\ue72d',
         '&Uosup;': '\ue32d', '&uvsup;': '\ue8ec', '&uwsup;': '\ue8ed',
         '&venl;': '\ueef8', '&vscap;': 'ᴠ', '&vbar;': '\ue74e',
         '&vslash;': '\ue8ba', '&vslashura;': '\ue8bb',
         '&vslashuradbl;': '\ue8bc', '&vdiagstrok;': 'ꝟ', '&Vdiagstrok;': 'Ꝟ',
         '&Vslstrok;': '℣', '&vdotbl;': 'ṿ', '&Vdotbl;': 'Ṿ',
         '&vdot;': '\ue74c', '&Vdot;': '\ue34c', '&vuml;': '\ue742',
         '&Vuml;': '\ue342', '&vacute;': '\ue73a', '&Vacute;': '\ue33a',
         '&vvertline;': '\ue74f', '&Vvertline;': '\ue34e',
         '&vdblac;': '\ue74b', '&Vdblac;': '\ue34b', '&vcirc;': '\ue73b',
         '&Vcirc;': '\ue33b', '&vring;': '\ue743', '&vmacr;': '\ue74d',
         '&Vmacr;': '\ue34d', '&Vovlhigh;': '\uf7b2', '&wynn;': 'ƿ',
         '&WYNN;': 'Ƿ', '&vins;': 'ꝩ', '&Vins;': 'Ꝩ', '&vinsdotbl;': '\ue7e6',
         '&Vinsdotbl;': '\ue3e6', '&vinsdot;': '\ue7e7', '&Vinsdot;': '\ue3e7',
         '&vinsacute;': '\uebbb', '&Vinsacute;': '\uebba', '&vwelsh;': 'ỽ',
         '&Vwelsh;': 'Ỽ', '&wenl;': '\ueef9', '&wscap;': 'ᴡ', '&wdotbl;': 'ẉ',
         '&Wdotbl;': 'Ẉ', '&wdot;': 'ẇ', '&Wdot;': 'Ẇ', '&wuml;': 'ẅ',
         '&Wuml;': 'Ẅ', '&wacute;': 'ẃ', '&Wacute;': 'Ẃ',
         '&wdblac;': '\ue750', '&Wdblac;': '\ue350', '&wgrave;': 'ẁ',
         '&Wgrave;': 'Ẁ', '&wcirc;': 'ŵ', '&Wcirc;': 'Ŵ', '&wring;': 'ẘ',
         '&wmacr;': '\ue757', '&Wmacr;': '\ue357', '&wasup;': '\ue8f0',
         '&wesup;': '\ue753', '&Wesup;': '\ue353', '&wisup;': '\ue8f1',
         '&wosup;': '\ue754', '&wusup;': '\ue8f2', '&wvsup;': '\ue8f3',
         '&xenl;': '\ueefa', '&xscap;': '\uef11', '&xmod;': 'ˣ', '&xdes;': 'ꭗ',
         '&xslashula;': '\ue8bd', '&xslashlra;': '\ue8be',
         '&xslashlradbl;': '\ue8ce', '&Xovlhigh;': '\uf7b3',
         '&yenl;': '\ueefb', '&yscap;': 'ʏ', '&ybar;': '\ue77b',
         '&ycurl;': '\ue785', '&Ycurl;': '\ue385', '&ydotbl;': 'ỵ',
         '&Ydotbl;': 'Ỵ', '&ydot;': 'ẏ', '&Ydot;': 'Ẏ', '&yuml;': 'ÿ',
         '&Yuml;': 'Ÿ', '&yacute;': 'ý', '&Yacute;': 'Ý', '&ydblac;': '\ue77c',
         '&Ydblac;': '\ue37c', '&ydotacute;': '\ue784',
         '&Ydotacute;': '\ue384', '&ygrave;': 'ỳ', '&Ygrave;': 'Ỳ',
         '&ycirc;': 'ŷ', '&Ycirc;': 'Ŷ', '&yring;': 'ẙ', '&yhook;': 'ỷ',
         '&Yhook;': 'Ỷ', '&ybreve;': '\ue776', '&Ybreve;': '\ue376',
         '&ymacr;': 'ȳ', '&Ymacr;': 'Ȳ', '&ymacrbreve;': '\ue775',
         '&Ymacrbreve;': '\ue375', '&ymacracute;': '\ue773',
         '&Ymacracute;': '\ue373', '&yylig;': 'ꝡ', '&YYlig;': 'Ꝡ',
         '&yyliguml;': '\uebe9', '&YYliguml;': '\uebe8',
         '&yyligdblac;': '\uebcb', '&YYligdblac;': '\uebca',
         '&yesup;': '\ue781', '&yrgmainstrok;': '\uf233', '&yloop;': 'ỿ',
         '&Yloop;': 'Ỿ', '&zenl;': '\ueefc', '&zscap;': 'ᴢ', '&zstrok;': 'ƶ',
         '&Zstrok;': 'Ƶ', '&zdotbl;': 'ẓ', '&Zdotbl;': 'Ẓ', '&zdot;': 'ż',
         '&Zdot;': 'Ż', '&zvisigot;': 'ꝣ', '&Zvisigot;': 'Ꝣ', '&ezh;': 'ʒ',
         '&EZH;': 'Ʒ', '&yogh;': 'ȝ', '&YOGH;': 'Ȝ', '&thorn;': 'þ',
         '&THORN;': 'Þ', '&thornenl;': '\ueef6', '&thornscap;': '\uef15',
         '&thornbar;': 'ꝥ', '&THORNbar;': 'Ꝥ', '&thornovlmed;': '\ue7a2',
         '&thornbarslash;': '\uf149', '&THORNbarslash;': '\ue337',
         '&thornbardes;': 'ꝧ', '&THORNbardes;': 'Ꝧ', '&thorndotbl;': '\ue79f',
         '&THORNdotbl;': '\ue39f', '&thornacute;': '\ue737',
         '&thornslonglig;': '\ue734', '&thornslongligbar;': '\ue735',
         '&thornrarmlig;': '\ue8c1', '&frac14;': '¼', '&frac12;': '½',
         '&frac34;': '¾', '&sup0;': '⁰', '&sup1;': '¹', '&sup2;': '²',
         '&sup3;': '³', '&sup4;': '⁴', '&sup5;': '⁵', '&sup6;': '⁶',
         '&sup7;': '⁷', '&sup8;': '⁸', '&sup9;': '⁹', '&sub0;': '₀',
         '&sub1;': '₁', '&sub2;': '₂', '&sub3;': '₃', '&sub4;': '₄',
         '&sub5;': '₅', '&sub6;': '₆', '&sub7;': '₇', '&sub8;': '₈',
         '&sub9;': '₉', '&romnumCDlig;': 'ↀ', '&romnumDDlig;': 'ↁ',
         '&romnumDDdbllig;': 'ↂ', '&romnumCrev;': 'Ↄ',
         '&romnumCrevovl;': '\uf23f', '&romnumCdblbar;': '\uf2fe',
         '&romnumcdblbar;': '\uf2ff', '&Imod;': 'ᴵ', '&Vmod;': 'ⱽ',
         '&Xmod;': '\uf1bf', '&asup;': 'ͣ', '&aeligsup;': 'ᷔ',
         '&anligsup;': '\uf036', '&anscapligsup;': '\uf03a', '&aoligsup;': 'ᷕ',
         '&arligsup;': '\uf038', '&arscapligsup;': '\uf130', '&avligsup;': 'ᷖ',
         '&bsup;': '\uf012', '&bscapsup;': '\uf013', '&csup;': 'ͨ',
         '&ccedilsup;': 'ᷗ', '&dsup;': 'ͩ', '&drotsup;': 'ᷘ', '&ethsup;': 'ᷙ',
         '&dscapsup;': '\uf016', '&esup;': 'ͤ', '&eogonsup;': '\uf135',
         '&emacrsup;': '\uf136', '&fsup;': '\uf017', '&gsup;': 'ᷚ',
         '&gscapsup;': 'ᷛ', '&hsup;': 'ͪ', '&isup;': 'ͥ',
         '&inodotsup;': '\uf02f', '&jsup;': '\uf030', '&jnodotsup;': '\uf031',
         '&ksup;': 'ᷜ', '&kscapsup;': '\uf01c', '&lsup;': 'ᷝ',
         '&lscapsup;': 'ᷞ', '&msup;': 'ͫ', '&mscapsup;': 'ᷟ', '&nsup;': 'ᷠ',
         '&nscapsup;': 'ᷡ', '&osup;': 'ͦ', '&omacrsup;': '\uf13f',
         '&oslashsup;': '\uf032', '&oogonsup;': '\uf13e',
         '&orrotsup;': '\uf03e', '&orumsup;': '\uf03f', '&psup;': '\uf025',
         '&qsup;': '\uf033', '&rsup;': 'ͬ', '&rrotsup;': 'ᷣ',
         '&rumsup;': '\uf040', '&rscapsup;': 'ᷢ', '&ssup;': 'ᷤ',
         '&slongsup;': 'ᷥ', '&tsup;': 'ͭ', '&trotsup;': '\uf03b',
         '&tscapsup;': '\uf02a', '&usup;': 'ͧ', '&vsup;': 'ͮ',
         '&wsup;': '\uf03c', '&xsup;': 'ͯ', '&ysup;': '\uf02b', '&zsup;': 'ᷦ',
         '&thornsup;': '\uf03d', '&combgrave;': '̀', '&combacute;': '́',
         '&combcirc;': '̂', '&combcircdbl;': '᷍', '&combtilde;': '̃',
         '&combmacr;': '̄', '&combbreve;': '̆', '&combdot;': '̇',
         '&combuml;': '̈', '&combhook;': '̉', '&combring;': '̊',
         '&combdblac;': '̋', '&combsgvertl;': '̍', '&combdbvertl;': '̎',
         '&combdotbl;': '̣', '&combced;': '̧', '&dblbarbl;': '̳',
         '&dblovl;': '̿', '&combogon;': '̨', '&combastbl;': '͙',
         '&combdblbrevebl;': '͜', '&combtripbrevebl;': '\uf1fc',
         '&combcurl;': '᷎', '&combcurlhigh;': '\uf1c5',
         '&combdothigh;': '\uf1ca', '&combcurlbar;': '\uf1cc', '&bar;': '̅',
         '&macrhigh;': '\uf00a', '&macrmed;': '\uf00b', '&ovlhigh;': '\uf00c',
         '&ovlmed;': '\uf00d', '&barbl;': '̲', '&baracr;': '̶',
         '&arbar;': '\uf1c0', '&combcomma;': '̕', '&combtildevert;': '̾',
         '&er;': '͛', '&erang;': '\uf1c7', '&ercurl;': '\uf1c8',
         '&ersub;': '᷏', '&ra;': 'ᷓ', '&rabar;': '\uf1c1', '&urrot;': '\uf153',
         '&urlemn;': '\uf1c2', '&ur;': '᷑', '&us;': '᷒', '&combisbelow;': '᷐',
         '&period;': '.', '&semi;': ';', '&amp;': '&', '&Theta;': 'Θ',
         '&theta;': 'θ', '&obiit;': 'ꝋ', '&OBIIT;': 'Ꝋ', '&et;': '⁊',
         '&etslash;': '\uf158', '&ET;': '\uf142', '&ETslash;': '\uf1a7',
         '&apomod;': 'ʼ', '&esse;': '≈', '&est;': '∻', '&condes;': 'ꝯ',
         '&CONdes;': 'Ꝯ', '&condot;': 'ꜿ', '&CONdot;': 'Ꜿ',
         '&usbase;': '\uf1a6', '&USbase;': '\uf1a5', '&usmod;': 'ꝰ',
         '&autem;': '\ue8a3', '&rum;': 'ꝝ', '&RUM;': 'Ꝝ', '&de;': '\uf159',
         '&is;': 'ꝭ', '&IS;': 'Ꝭ', '&sstrok;': 'ꝸ', '&etfin;': 'ꝫ',
         '&ETfin;': 'Ꝫ', '&sem;': '\uf1ac', '&fMedrun;': 'ᚠ', '&mMedrun;': 'ᛘ',
         '&lbbar;': '℔', '&circ;': '^', '&acute;': '´', '&grave;': '`',
         '&uml;': '¨', '&tld;': '~', '&macr;': '¯', '&breve;': '˘',
         '&dot;': '˙', '&ring;': '˚', '&cedil;': '¸', '&ogon;': '˛',
         '&tilde;': '˜', '&dblac;': '˝', '&verbarup;': 'ˈ', '&middot;': '·',
         '&hyphpoint;': '‧', '&sgldr;': '․', '&dblldr;': '‥', '&hellip;': '…',
         '&colon;': ':', '&comma;': ',', '&tridotright;': '჻',
         '&tridotupw;': '∴', '&tridotdw;': '∵', '&quaddot;': '∷',
         '&tridotleft;': '⁖', '&lozengedot;': '⁘', '&midring;': '\uf1da',
         '&verbar;': '|', '&brvbar;': '¦', '&Verbar;': '‖', '&sol;': '/',
         '&fracsol;': '⁄', '&dblsol;': '⫽', '&bsol;': '\\', '&luslst;': '⸌',
         '&ruslst;': '⸍', '&rlslst;': '⸜', '&llslst;': '⸝', '&lowbar;': '_',
         '&hyphen;': '-', '&dash;': '‐', '&nbhy;': '‑', '&dblhyph;': '⹀',
         '&dbloblhyph;': '⸗', '&numdash;': '‒', '&ndash;': '–', '&mdash;': '—',
         '&horbar;': '―', '&excl;': '!', '&iexcl;': '¡', '&quest;': '?',
         '&iquest;': '¿', '&ramus;': '\uf1db', '&lpar;': '(', '&rpar;': ')',
         '&lUbrack;': '⸦', '&rUbrack;': '⸧', '&ldblpar;': '⸨',
         '&rdblpar;': '⸩', '&lsqb;': '[', '&rsqb;': ']', '&lcub;': '{',
         '&rcub;': '}', '&lsqbqu;': '⁅', '&rsqbqu;': '⁆', '&lwhsqb;': '⟦',
         '&rwhsqb;': '⟧', '&verbarql;': '⸡', '&verbarqr;': '⸠',
         '&luhsqb;': '⸢', '&ruhsqb;': '⸣', '&llhsqb;': '⸤', '&rlhsqb;': '⸥',
         '&apos;': "'", '&prime;': '′', '&quot;': '"', '&Prime;': '″',
         '&lsquo;': '‘', '&rsquo;': '’', '&lsquolow;': '‚', '&rsquorev;': '‛',
         '&ldquo;': '“', '&rdquo;': '”', '&ldquolow;': '„', '&rdquorev;': '‟',
         '&lsaquo;': '‹', '&laquo;': '«', '&lt;': '<', '&langb;': '⟨',
         '&rsaquo;': '›', '&gt;': '>', '&raquo;': '»', '&rangb;': '⟩',
         '&hidot;': '\uf1f8', '&posit;': '\uf1e2', '&ductsimpl;': '\uf1e3',
         '&punctvers;': '\uf1ea', '&punctposit;': '\uf1e4',
         '&colmidcomposit;': '\uf1e5', '&bidotscomposit;': '\uf1f2',
         '&tridotscomposit;': '\uf1e6', '&punctelev;': '\uf161',
         '&punctelevdiag;': '\uf1f0', '&punctelevhiback;': '\uf1fa',
         '&punctelevhack;': '\uf1fb', '&punctflex;': '\uf1f5',
         '&punctexclam;': '\uf1e7', '&punctinter;': '\uf160',
         '&punctintertilde;': '\uf1e8', '&punctinterlemn;': '\uf1f1',
         '&punctpercont;': '⸮', '&wavylin;': '\uf1f9', '&medcom;': '\uf1e0',
         '&parag;': '\uf1e1', '&renvoi;': '\uf1ec', '&tridotsdownw;': '⸪',
         '&tridotsupw;': '⸫', '&quaddots;': '⸬', '&fivedots;': '⸭',
         '&virgsusp;': '\uf1f4', '&virgmin;': '\uf1f7', '&dipledot;': '⋗',
         '&sp;': ' ', '&nbsp;': '\xa0', '&nnbsp;': '\u202f',
         '&enqd;': '\u2000', '&emqd;': '\u2001', '&ensp;': '\u2002',
         '&emsp;': '\u2003', '&emsp13;': '\u2004', '&emsp14;': '\u2005',
         '&emsp16;': '\u2006', '&numsp;': '\u2007', '&puncsp;': '\u2008',
         '&thinsp;': '\u2009', '&hairsp;': '\u200a', '&zerosp;': '\u200b',
         '&del;': '\x7f', '&shy;': '\xad', '&num;': '#', '&sect;': '§',
         '&ast;': '*', '&triast;': '⁂', '&commat;': '@', '&copy;': '©',
         '&reg;': '®', '&not;': '¬', '&logand;': '∧', '&para;': '¶',
         '&revpara;': '⁋', '&cross;': '✝', '&dagger;': '†', '&Dagger;': '‡',
         '&tridagger;': '\uf1d2', '&refmark;': '※', '&dotcross;': '⁜',
         '&hedera;': '❦', '&hederarot;': '❧', '&dollar;': '$', '&cent;': '¢',
         '&pound;': '£', '&curren;': '¤', '&yen;': '¥', '&pennygerm;': '₰',
         '&scruple;': '℈', '&romaslibr;': '\uf2e0', '&romXbar;': '\uf2e1',
         '&romscapxbar;': '\uf2e2', '&romscapybar;': '\uf2e3',
         '&romscapdslash;': '\uf2e4', '&drotbar;': '\uf159', '&ecu;': '\uf2e7',
         '&florloop;': '\uf2e8', '&grosch;': '\uf2e9', '&helbing;': '\uf2fb',
         '&krone;': '\uf2fa', '&libradut;': '\uf2ea', '&librafren;': '\uf2eb',
         '&libraital;': '\uf2ec', '&libraflem;': '\uf2ed',
         '&liranuov;': '\uf2ee', '&lirasterl;': '\uf2ef',
         '&markold;': '\uf2f0', '&markflour;': '\uf2f1', '&msign;': '\uf2f2',
         '&msignflour;': '\uf2f3', '&penningar;': '\uf2f5',
         '&reichtalold;': '\uf2f6', '&schillgerm;': '\uf2f7',
         '&schillgermscript;': '\uf2f8', '&scudi;': '\uf2f9', '&ounce;': '℥',
         '&sestert;': '\uf2fa', '&romas;': '\uf2d8', '&romunc;': '\uf2d9',
         '&romsemunc;': '\uf2da', '&romsext;': '\uf2db',
         '&romdimsext;': '\uf2dc', '&romsiliq;': '\uf2dd',
         '&romquin;': '\uf2de', '&romdupond;': '\uf2df', '&plus;': '+',
         '&minus;': '−', '&plusmn;': '±', '&times;': '×', '&divide;': '÷',
         '&equals;': '=', '&infin;': '∞', '&notequals;': '≠', '&percnt;': '%',
         '&permil;': '‰', '&deg;': '°', '&smallzero;': '\uf1bd',
         '&micro;': 'µ', '&dram;': '\uf2e6', '&obol;': '\uf2f4',
         '&sextans;': '\uf2fb', '&ouncescript;': '\uf2fd', '&arrsgllw;': '←',
         '&arrsglupw;': '↑', '&arrsglrw;': '→', '&arrsgldw;': '↓',
         '&squareblsm;': '▪', '&squarewhsm;': '▫', '&bull;': '•',
         '&circledot;': '◌', '&tribull;': '‣', '&trirightwh;': '▹',
         '&trileftwh;': '◃', '&metrshort;': '⏑', '&metrshortlong;': '⏒',
         '&metrlongshort;': '⏓', '&metrdblshortlong;': '⏔',
         '&metranc;': '\uf70a', '&metrancacute;': '\uf70b',
         '&metrancdblac;': '\uf719', '&metrancgrave;': '\uf70c',
         '&metrancdblgrave;': '\uf71a', '&metrbreve;': '\uf701',
         '&metrbreveacute;': '\uf706', '&metrbrevedblac;': '\uf717',
         '&metrbrevegrave;': '\uf707', '&metrbrevedblgrave;': '\uf718',
         '&metrmacr;': '\uf700', '&metrmacracute;': '\uf704',
         '&metrmacrdblac;': '\uf715', '&metrmacrgrave;': '\uf705',
         '&metrmacrdblgrave;': '\uf716', '&metrmacrbreve;': '\uf702',
         '&metrbrevemacr;': '\uf703', '&metrmacrbreveacute;': '\uf708',
         '&metrmacrbrevegrave;': '\uf709', '&metrdblbrevemacr;': '\uf72e',
         '&metrdblbrevemacracute;': '\uf71b',
         '&metrdblbrevemacrdblac;': '\uf71c', '&metrpause;': '\uf714'}

MUFI4_KEYS = "&aenl;&ascap;&ordf;&aogon;&Aogon;&acurl;&Acurl;&adotbl;" \
             "&Adotbl;&adot;&Adot;&auml;&Auml;&adiaguml;&adotbluml;&aacute;" \
             "&Aacute;&aenlacute;&aogonacute;&Aogonacute;&adblac;&Adblac;" \
             "&adotacute;&Adotacute;&agrave;&Agrave;&acirc;&Acirc;&aumlcirc;" \
             "&aringcirc;&atilde;&Atilde;&aring;&Aring;&ahook;&Ahook;" \
             "&abreve;&Abreve;&amacr;&Amacr;&amacrbreve;&Amacrbreve;" \
             "&abreveacute;&Abreveacute;&amacracute;&Amacracute;&aalig;" \
             "&aacloselig;&AAlig;&aaligenl;&aaligdotbl;&AAligdotbl;" \
             "&aaligdot;&AAligdot;&aaliguml;&AAliguml;&aaligacute;" \
             "&AAligacute;&aaligdblac;&AAligdblac;&aelig;&AElig;&aeligenl;" \
             "&aeligscap;&aeligred;&aeligcurl;&AEligcurl;&aeligogon;" \
             "&AEligogon;&aeligdotbl;&AEligdotbl;&aeligdot;&AEligdot;" \
             "&aeliguml;&AEliguml;&aeligacute;&AEligacute;&aeligogonacute;" \
             "&aeligdblac;&AEligdblac;&aeligring;&aeligbreve;&AEligbreve;" \
             "&aeligmacr;&AEligmacr;&aeligmacrbreve;&AEligmacrbreve;" \
             "&aeligmacracute;&AEligmacracute;&aeligdotacute;&AEligdotacute;" \
             "&aflig;&afinslig;&aglig;&allig;&anlig;&anscaplig;&aolig;" \
             "&AOlig;&aoligenl;&aenlosmalllig;&aoligred;&AOligred;" \
             "&aoligdotbl;&AOligdotbl;&aoligacute;&AOligacute;&aoligdblac;" \
             "&AOligdblac;&aplig;&arlig;&arscaplig;&aulig;&AUlig;" \
             "&auligdotbl;&AUligdotbl;&auligacute;&AUligacute;&avlig;&AVlig;" \
             "&avligslash;&AVligslash;&avligslashacute;&AVligslashacute;" \
             "&avligogon;&AVligogon;&avligdotbl;&AVligdotbl;&avligacute;" \
             "&AVligacute;&avligdblac;&AVligdblac;&aylig;&AYlig;&ayligdotbl;" \
             "&AYligdotbl;&ayligdot;&AYligdot;&athornlig;&aesup;&Aesup;" \
             "&iesup;&aosup;&ausup;&avsup;&aunc;&aopen;&ains;&Ains;" \
             "&aneckless;&anecklesselig;&AnecklessElig;&anecklessvlig;" \
             "&aclose;&Asqu;&benl;&bscap;&bscapdot;&bscapdotbl;&bdotbl;" \
             "&Bdotbl;&bdot;&Bdot;&bacute;&Bacute;&bstrok;&bovlmed;&bblig;" \
             "&bglig;&cenl;&cscap;&ccedil;&Ccedil;&cogon;&Cogon;&cdotbl;" \
             "&Cdotbl;&cdot;&Cdot;&cacute;&Cacute;&Covlhigh;&chlig;&cklig;" \
             "&ctlig;&Csqu;&ccurl;&CONbase;&conbase;&denl;&dscap;&dstrok;" \
             "&Dstrok;&dovlmed;&dtailstrok;&dtail;&dscapdot;&ddotbl;&Ddotbl;" \
             "&dscapdotbl;&ddot;&Ddot;&dacute;&Dacute;&eth;&ETH;&ethenl;" \
             "&ethscap;&ethdotbl;&ETHdotbl;&Dovlhigh;&drotdrotlig;&Drot;" \
             "&drot;&drotdot;&drotacute;&drotenl;&dscript;&dcurl;&eenl;" \
             "&escap;&eogon;&Eogon;&ecurl;&Ecurl;&eogoncurl;&Eogoncurl;" \
             "&edotbl;&Edotbl;&eogondot;&Eogondot;&eogondotbl;&Eogondotbl;" \
             "&eogonenl;&edot;&Edot;&euml;&Euml;&eumlmacr;&eacute;&Eacute;" \
             "&eogonacute;&Eogonacute;&edotblacute;&edblac;&Edblac;" \
             "&edotacute;&Edotacute;&eogondotacute;&Eogondotacute;" \
             "&eogondblac;&Eogondblac;&egrave;&Egrave;&ecirc;&Ecirc;" \
             "&eogoncirc;&ering;&ebreve;&Ebreve;&emacr;&Emacr;&eogonmacr;" \
             "&Eogonmacr;&emacrbreve;&Emacrbreve;&emacracute;&Emacracute;" \
             "&eylig;&eacombcirc;&eucombcirc;&easup;&Easup;&eesup;&eisup;" \
             "&eosup;&evsup;&schwa;&Eunc;&Euncclose;&eunc;&eext;&etall;" \
             "&fenl;&fscap;&fdotbl;&Fdotbl;&fdot;&Fdot;&fscapdot;&facute;" \
             "&Facute;&faumllig;&fflig;&filig;&fjlig;&foumllig;" \
             "&fllig;&frlig;&ftlig;&fuumllig;&fylig;&ffilig;&ffllig;&fftlig;" \
             "&ffylig;&ftylig;&fturn;&Fturn;&Frev;&fins;&Fins;&finsenl;" \
             "&finsdot;&Finsdot;&finsdothook;&finssemiclose;" \
             "&finssemiclosedot;&finsclose;&finsclosedot;&finsdotbl;" \
             "&Finsdotbl;&finsacute;&Finsacute;&fcurl;&genl;&gscap;&gstrok;" \
             "&Gstrok;&gdotbl;&Gdotbl;&gscapdotbl;&gdot;&Gdot;&gscapdot;" \
             "&Gacute;&gacute;&gglig;&gdlig;&gdrotlig;&gethlig;&golig;" \
             "&gplig;&grlig;&gins;&Gins;&ginsturn;&Ginsturn;&Gsqu;&gdivloop;" \
             "&glglowloop;&gsmlowloop;&gopen;&gcurl;&henl;&hscap;&hhook;" \
             "&hstrok;&hovlmed;&hdotbl;&Hdotbl;&Hdot;&hdot;&hscapdot;" \
             "&hacute;&Hacute;&hwair;&HWAIR;&hslonglig;&hslongligbar;" \
             "&hrarmlig;&Hrarmlig;&hhalf;&Hhalf;&Hunc;&hrdes;&ienl;&iscap;" \
             "&inodot;&inodotenl;&Idot;&istrok;&idblstrok;&iogon;" \
             "&inodotogon;&Iogon;&icurl;&Icurl;&idotbl;&Idotbl;&ibrevinvbl;" \
             "&iuml;&Iuml;&iacute;&Iacute;&idblac;&Idblac;&idotacute;" \
             "&Idotacute;&igrave;&Igrave;&icirc;&Icirc;&ihook;&Ihook;" \
             "&ibreve;&Ibreve;&imacr;&Imacr;&iovlmed;&Iovlhigh;&imacrbreve;" \
             "&Imacrbreve;&imacracute;&Imacracute;&ijlig;&IJlig;&iasup;" \
             "&iosup;&iusup;&ivsup;&ilong;&Ilong;&jenl;&jscap;&jnodot;" \
             "&jnodotenl;&Jdot;&jnodotstrok;&jbar;&jdblstrok;&Jbar;&jcurl;" \
             "&Jcurl;&juml;&Juml;&jdotbl;&Jdotbl;&jacute;&Jacute;&jdblac;" \
             "&Jdblac;&jmacrmed;&jovlmed;&Jmacrhigh;&Jovlhigh;&jesup;&kenl;" \
             "&kscap;&khook;&kbar;&Kbar;&kovlmed;&kstrleg;&Kstrleg;" \
             "&kstrascleg;&Kstrascleg;&kdot;&Kdot;&kscapdot;&kdotbl;&Kdotbl;" \
             "&kacute;&Kacute;&kslonglig;&kslongligbar;&krarmlig;&kunc;" \
             "&ksemiclose;&kclose;&kcurl;&lenl;&lscap;&lbar;&lstrok;&Lstrok;" \
             "&lhighstrok;&Lhighstrok;&lovlmed;&ltailstrok;&ldotbl;&Ldotbl;" \
             "&lscapdotbl;&ldot;&Ldot;&lscapdot;&lacute;&Lacute;&lringbl;" \
             "&lmacrhigh;&lovlhigh;&Lovlhigh;&lbrk;&Lbrk;&llwelsh;&LLwelsh;" \
             "&lllig;&ldes;&lturn;&Lturn;&menl;&mscap;&mtailstrok;&mdotbl;" \
             "&Mdotbl;&mscapdotbl;&mdot;&Mdot;&mscapdot;&macute;&Macute;" \
             "&mringbl;&mmacrmed;&Mmacrhigh;&movlmed;&Movlhigh;&mesup;&Minv;" \
             "&mturn;&Mturn;&munc;&mmedunc;&Munc;&mrdes;&muncdes;" \
             "&mmeduncdes;&Muncdes;&muncacute;&mmeduncacute;&Muncacute;" \
             "&M5leg;&nenl;&nscap;&nscapldes;&nlrleg;&nlfhook;&nbar;" \
             "&ntailstrok;&ndot;&Ndot;&nscapdot;&nacute;&Nacute;&ndotbl;" \
             "&Ndotbl;&nscapdotbl;&ncirc;&ntilde;&Ntilde;&nringbl;&nmacrmed;" \
             "&Nmacrhigh;&eng;&ENG;&nscapslonglig;&nrdes;&Nrdes;&nscaprdes;" \
             "&nflour;&oenl;&oscap;&ordm;&oogon;&Oogon;&ocurl;&Ocurl;" \
             "&oogoncurl;&Oogoncurl;&ocurlacute;&Ocurlacute;&oslash;&Oslash;" \
             "&oslashcurl;&Oslashcurl;&oslashogon;&Oslashogon;&odotbl;" \
             "&Odotbl;&oslashdotbl;&Oslashdotbl;&odot;&Odot;&oogondot;" \
             "&Oogondot;&oogonmacr;&Oogonmacr;&oslashdot;&Oslashdot;" \
             "&oogondotbl;&Oogondotbl;&ouml;&Ouml;&odiaguml;&oumlacute;" \
             "&oacute;&Oacute;&oslashacute;&Oslashacute;&oslashdblac;" \
             "&Oslashdblac;&oogonacute;&Oogonacute;&oslashogonacute;" \
             "&Oslashogonacute;&odblac;&Odblac;&odotacute;&Odotacute;" \
             "&oogondotacute;&Oogondotacute;&oslashdotacute;&Oslashdotacute;" \
             "&oogondblac;&Oogondblac;&ograve;&Ograve;&ocirc;&Ocirc;" \
             "&oumlcirc;&Oumlcirc;&oogoncirc;&ocar;&Ocar;&otilde;&Otilde;" \
             "&oring;&ohook;&Ohook;&obreve;&Obreve;&oslashbreve;" \
             "&Oslashbreve;&omacr;&Omacr;&oslashmacr;&Oslashmacr;" \
             "&omacrbreve;&Omacrbreve;&oslashmacrbreve;&Oslashmacrbreve;" \
             "&omacracute;&Omacracute;&oslashmacracute;&Oslashmacracute;" \
             "&oumlmacr;&Oumlmacr;&oclig;&oelig;&OElig;&oeligscap;&oeligenl;" \
             "&oeligogon;&OEligogon;&Oloop;&oloop;&oeligacute;&OEligacute;" \
             "&oeligdblac;&OEligdblac;&oeligmacr;&OEligmacr;&oeligmacrbreve;" \
             "&OEligmacrbreve;&oolig;&OOlig;&ooliguml;&OOliguml;&ooligacute;" \
             "&OOligacute;&ooligdblac;&OOligdblac;&ooligdotbl;&OOligdotbl;" \
             "&orrotlig;&oasup;&oesup;&Oesup;&oisup;&oosup;&ousup;&Ousup;" \
             "&ovsup;&oopen;&oopenmacr;&penl;&pscap;&pbardes;&Pbardes;" \
             "&pflour;&Pflour;&psquirrel;&Psquirrel;&pdotbl;&Pdotbl;&pdot;" \
             "&Pdot;&pscapdot;&pacute;&Pacute;&pdblac;&Pdblac;&pmacr;&pplig;" \
             "&PPlig;&ppflourlig;&ppliguml;&PPliguml;&Prev;&qenl;&qscap;" \
             "&qslstrok;&Qslstrok;&qbardes;&Qbardes;&qbardestilde;&q2app;" \
             "&q3app;&qcentrslstrok;&qdotbl;&Qdotbl;&qdot;&Qdot;&qmacr;" \
             "&qvinslig;&Qstem;&renl;&rscap;&YR;&rdes;&rdesstrok;" \
             "&rtailstrok;&rscaptailstrok;&Rtailstrok;&Rslstrok;&rdotbl;" \
             "&Rdotbl;&rdot;&Rdot;&rscapdot;&racute;&Racute;&rringbl;" \
             "&rscapdotbl;&resup;&rrot;&Rrot;&rrotdotbl;&rrotacute;&rins;" \
             "&Rins;&rflour;&senl;&sscap;&sdot;&Sdot;&sscapdot;&sacute;" \
             "&Sacute;&sdotbl;&Sdotbl;&sscapdotbl;&szlig;&SZlig;" \
             "&slongaumllig;&slongchlig;&slonghlig;&slongilig;&slongjlig;" \
             "&slongklig;&slongllig;&slonglbarlig;&slongoumllig;&slongplig;" \
             "&slongslig;&slongslonglig;&slongslongilig;&slongslongklig;&" \
             "slongslongllig;&slongslongtlig;&stlig;&slongtlig;&slongtilig;" \
             "&slongtrlig;&slonguumllig;&slongvinslig;&slongdestlig;&slong;" \
             "&slongenl;&slongbarslash;&slongbar;&slongovlmed;&slongslstrok;" \
             "&slongflour;&slongacute;&slongdes;&slongdotbl;&Sclose;&sclose;" \
             "&sins;&Sins;&tenl;&tscap;&ttailstrok;&togon;&Togon;&tdotbl;" \
             "&Tdotbl;&tdot;&Tdot;&tscapdot;&tscapdotbl;&tacute;&Tacute;" \
             "&trlig;&ttlig;&trottrotlig;&tylig;&tzlig;&trot;&Trot;&tcurl;" \
             "&uenl;&uscap;&ubar;&uogon;&Uogon;&ucurl;&Ucurl;&udotbl;" \
             "&Udotbl;&ubrevinvbl;&udot;&Udot;&uuml;&Uuml;&uacute;&Uacute;" \
             "&udblac;&Udblac;&udotacute;&Udotacute;&ugrave;&Ugrave;" \
             "&uvertline;&Uvertline;&ucirc;&Ucirc;&uumlcirc;&Uumlcirc;&ucar;" \
             "&Ucar;&uring;&Uring;&uhook;&Uhook;&ucurlbar;&ubreve;&Ubreve;" \
             "&umacr;&Umacr;&umacrbreve;&Umacrbreve;&umacracute;&Umacracute;" \
             "&uumlmacr;&Uumlmacr;&uelig;&UElig;&uulig;&UUlig;&uuligdblac;" \
             "&UUligdblac;&uasup;&uesup;&Uesup;&uisup;&uosup;&Uosup;&uvsup;" \
             "&uwsup;&venl;&vscap;&vbar;&vslash;&vslashura;&vslashuradbl;" \
             "&vdiagstrok;&Vdiagstrok;&Vslstrok;&vdotbl;&Vdotbl;&vdot;&Vdot;" \
             "&vuml;&Vuml;&vacute;&Vacute;&vvertline;&Vvertline;&vdblac;" \
             "&Vdblac;&vcirc;&Vcirc;&vring;&vmacr;&Vmacr;&Vovlhigh;&wynn;" \
             "&WYNN;&vins;&Vins;&vinsdotbl;&Vinsdotbl;&vinsdot;&Vinsdot;" \
             "&vinsacute;&Vinsacute;&vwelsh;&Vwelsh;&wenl;&wscap;&wdotbl;" \
             "&Wdotbl;&wdot;&Wdot;&wuml;&Wuml;&wacute;&Wacute;&wdblac;" \
             "&Wdblac;&wgrave;&Wgrave;&wcirc;&Wcirc;&wring;&wmacr;&Wmacr;" \
             "&wasup;&wesup;&Wesup;&wisup;&wosup;&wusup;&wvsup;&xenl;&xscap;" \
             "&xmod;&xdes;&xslashula;&xslashlra;&xslashlradbl;&Xovlhigh;" \
             "&yenl;&yscap;&ybar;&ycurl;&Ycurl;&ydotbl;&Ydotbl;&ydot;&Ydot" \
             ";&yuml;&Yuml;&yacute;&Yacute;&ydblac;&Ydblac;&ydotacute;" \
             "&Ydotacute;&ygrave;&Ygrave;&ycirc;&Ycirc;&yring;&yhook;&Yhook;" \
             "&ybreve;&Ybreve;&ymacr;&Ymacr;&ymacrbreve;&Ymacrbreve;" \
             "&ymacracute;&Ymacracute;&yylig;&YYlig;&yyliguml;&YYliguml;" \
             "&yyligdblac;&YYligdblac;&yesup;&yrgmainstrok;&yloop;&Yloop;" \
             "&zenl;&zscap;&zstrok;&Zstrok;&zdotbl;&Zdotbl;&zdot;&Zdot;" \
             "&zvisigot;&Zvisigot;&ezh;&EZH;&yogh;&YOGH;&thorn;&THORN;" \
             "&thornenl;&thornscap;&thornbar;&THORNbar;&thornovlmed;" \
             "&thornbarslash;&THORNbarslash;&thornbardes;&THORNbardes;" \
             "&thorndotbl;&THORNdotbl;&thornacute;&thornslonglig;" \
             "&thornslongligbar;&thornrarmlig;&frac14;&frac12;&frac34;&sup0;" \
             "&sup1;&sup2;&sup3;&sup4;&sup5;&sup6;&sup7;&sup8;&sup9;&sub0;" \
             "&sub1;&sub2;&sub3;&sub4;&sub5;&sub6;&sub7;&sub8;&sub9;" \
             "&romnumCDlig;&romnumDDlig;&romnumDDdbllig;&romnumCrev;" \
             "&romnumCrevovl;&romnumCdblbar;&romnumcdblbar;&Imod;&Vmod;" \
             "&Xmod;&asup;&aeligsup;&anligsup;&anscapligsup;&aoligsup;" \
             "&arligsup;&arscapligsup;&avligsup;&bsup;&bscapsup;&csup;" \
             "&ccedilsup;&dsup;&drotsup;&ethsup;&dscapsup;&esup;&eogonsup;" \
             "&emacrsup;&fsup;&gsup;&gscapsup;&hsup;&isup;&inodotsup;&jsup;" \
             "&jnodotsup;&ksup;&kscapsup;&lsup;&lscapsup;&msup;&mscapsup;" \
             "&nsup;&nscapsup;&osup;&omacrsup;&oslashsup;&oogonsup;" \
             "&orrotsup;&orumsup;&psup;&qsup;&rsup;&rrotsup;&rumsup;" \
             "&rscapsup;&ssup;&slongsup;&tsup;&trotsup;&tscapsup;&usup;" \
             "&vsup;&wsup;&xsup;&ysup;&zsup;&thornsup;&combgrave;&combacute;" \
             "&combcirc;&combcircdbl;&combtilde;&combmacr;&combbreve;" \
             "&combdot;&combuml;&combhook;&combring;&combdblac;&combsgvertl;" \
             "&combdbvertl;&combdotbl;&combced;&dblbarbl;&dblovl;&combogon;" \
             "&combastbl;&combdblbrevebl;&combtripbrevebl;&combcurl;" \
             "&combcurlhigh;&combdothigh;&combcurlbar;&bar;&macrhigh;" \
             "&macrmed;&ovlhigh;&ovlmed;&barbl;&baracr;&arbar;&combcomma;" \
             "&combtildevert;&er;&erang;&ercurl;&ersub;&ra;&rabar;&urrot;" \
             "&urlemn;&ur;&us;&combisbelow;&period;&semi;&amp;&Theta;&theta;" \
             "&obiit;&OBIIT;&et;&etslash;&ET;&ETslash;&apomod;&esse;&est;" \
             "&condes;&CONdes;&condot;&CONdot;&usbase;&USbase;&usmod;&autem;" \
             "&rum;&RUM;&de;&is;&IS;&sstrok;&etfin;&ETfin;&sem;&fMedrun;" \
             "&mMedrun;&lbbar;&circ;&acute;&grave;&uml;&tld;&macr;&breve;" \
             "&dot;&ring;&cedil;&ogon;&tilde;&dblac;&verbarup;&middot;" \
             "&hyphpoint;&sgldr;&dblldr;&hellip;&colon;&comma;&tridotright;" \
             "&tridotupw;&tridotdw;&quaddot;&tridotleft;&lozengedot;" \
             "&midring;&verbar;&brvbar;&Verbar;&sol;&fracsol;&dblsol;&bsol;" \
             "&luslst;&ruslst;&rlslst;&llslst;&lowbar;&hyphen;&dash;&nbhy;" \
             "&dblhyph;&dbloblhyph;&numdash;&ndash;&mdash;&horbar;&excl;" \
             "&iexcl;&quest;&iquest;&ramus;&lpar;&rpar;&lUbrack;&rUbrack;" \
             "&ldblpar;&rdblpar;&lsqb;&rsqb;&lcub;&rcub;&lsqbqu;&rsqbqu;" \
             "&lwhsqb;&rwhsqb;&verbarql;&verbarqr;&luhsqb;&ruhsqb;&llhsqb;" \
             "&rlhsqb;&apos;&prime;&quot;&Prime;&lsquo;&rsquo;&lsquolow;" \
             "&rsquorev;&ldquo;&rdquo;&ldquolow;&rdquorev;&lsaquo;&laquo;" \
             "&lt;&langb;&rsaquo;&gt;&raquo;&rangb;&hidot;&posit;&ductsimpl;" \
             "&punctvers;&punctposit;&colmidcomposit;&bidotscomposit;" \
             "&tridotscomposit;&punctelev;&punctelevdiag;&punctelevhiback;" \
             "&punctelevhack;&punctflex;&punctexclam;&punctinter;" \
             "&punctintertilde;&punctinterlemn;&punctpercont;&wavylin;" \
             "&medcom;&parag;&renvoi;&tridotsdownw;&tridotsupw;&quaddots;" \
             "&fivedots;&virgsusp;&virgmin;&dipledot;&sp;&nbsp;&nnbsp;&enqd;" \
             "&emqd;&ensp;&emsp;&emsp13;&emsp14;&emsp16;&numsp;&puncsp;" \
             "&thinsp;&hairsp;&zerosp;&del;&shy;&num;&sect;&ast;&triast;" \
             "&commat;&copy;&reg;&not;&logand;&para;&revpara;&cross;&dagger;" \
             "&Dagger;&tridagger;&refmark;&dotcross;&hedera;&hederarot;" \
             "&dollar;&cent;&pound;&curren;&yen;&pennygerm;&scruple;" \
             "&romaslibr;&romXbar;&romscapxbar;&romscapybar;&romscapdslash;" \
             "&drotbar;&ecu;&florloop;&grosch;&helbing;&krone;&libradut;" \
             "&librafren;&libraital;&libraflem;&liranuov;&lirasterl;" \
             "&markold;&markflour;&msign;&msignflour;&penningar;" \
             "&reichtalold;&schillgerm;&schillgermscript;&scudi;&ounce;" \
             "&sestert;&romas;&romunc;&romsemunc;&romsext;&romdimsext;" \
             "&romsiliq;&romquin;&romdupond;&plus;&minus;&plusmn;&times;" \
             "&divide;&equals;&infin;&notequals;&percnt;&permil;&deg;" \
             "&smallzero;&micro;&dram;&obol;&sextans;&ouncescript;&arrsgllw;" \
             "&arrsglupw;&arrsglrw;&arrsgldw;&squareblsm;&squarewhsm;&bull;" \
             "&circledot;&tribull;&trirightwh;&trileftwh;&metrshort;" \
             "&metrshortlong;&metrlongshort;&metrdblshortlong;&metranc;" \
             "&metrancacute;&metrancdblac;&metrancgrave;&metrancdblgrave;" \
             "&metrbreve;&metrbreveacute;&metrbrevedblac;&metrbrevegrave;" \
             "&metrbrevedblgrave;&metrmacr;&metrmacracute;&metrmacrdblac;" \
             "&metrmacrgrave;&metrmacrdblgrave;&metrmacrbreve;" \
             "&metrbrevemacr;&metrmacrbreveacute;&metrmacrbrevegrave;" \
             "&metrdblbrevemacr;&metrdblbrevemacracute;" \
             "&metrdblbrevemacrdblac;&metrpause;"

MUFI4_VALS = "ᴀªąĄạẠȧȦäÄáÁàÀâÂãÃåÅảẢăĂāĀắẮꜳꜲ" \
             "æÆᴁǽǼǣǢ" \
             "ꜵꜴꜷꜶꜹꜸꜻꜺꜽꜼ" \
             "ʙḅḄḃḂƀᴄçÇċĊćĆ" \
             "ↃↄᴅđĐꝱɖḍḌḋḊðÐᴆꝹꝺẟᴇęĘẹẸ" \
             "ėĖëËéÉèÈêÊĕĔēĒḗḖəꜰḟ" \
             "ḞﬀﬁﬂﬃﬄⅎℲꟻꝼꝻɢǥǤġĠ" \
             "ǴǵᵹꝽꝿꝾɡʜɦħḥḤḣḢƕǶⱶⱵɪıİɨįĮ" \
             "ịỊïÏíÍìÌîÎỉỈĭĬīĪĳĲꟾᴊȷɟɉɈ" \
             "ᴋƙꝁꝀꝃꝂꝅꝄḳḲḱḰʟƚłŁꝉꝈꝲḷḶĺĹꝇꝆỻỺꞁ" \
             "ꞀᴍꝳṃṂṁṀḿḾꟽɯƜꟿɴƞɲꝴṅṄńŃṇṆ" \
             "ñÑŋŊᴏºǫǪøØọỌȯȮǭǬöÖóÓ" \
             "ǿǾőŐòÒôÔǒǑõÕỏỎŏŎōŌṓṒȫȪœ" \
             "ŒɶꝌꝍꝏꝎɔᴘꝑꝐꝓꝒꝕꝔṗṖṕ" \
             "ṔꟼꝙꝘꝗꝖʀƦɼꝵꝶ℞℟ṛṚṙṘŕŔꝛꝚ" \
             "ꞃꞂꜱṡṠśŚṣṢßẞﬆﬅſẜẝ" \
             "ꞅꞄᴛꝷṭṬṫṪꞇꞆᴜʉųŲụỤüÜúÚűŰùÙûÛ" \
             "ǔǓůŮủỦŭŬūŪǖǕᴠꝟꝞ℣ṿṾ" \
             "ƿǷꝩꝨỽỼᴡẉẈẇẆẅẄẃẂẁẀŵŴẘˣꭗʏỵỴẏẎ" \
             "ÿŸýÝỳỲŷŶẙỷỶȳȲꝡꝠỿỾᴢƶƵẓẒżŻꝣꝢʒƷȝȜþÞꝥꝤꝧꝦ" \
             "¼½¾⁰¹²³⁴⁵⁶⁷⁸⁹₀₁₂₃₄₅₆₇₈₉ↀↁↂↃᴵⱽͣᷔᷕᷖͨᷗͩᷘᷙͤᷚᷛͪͥ" \
             "ᷜᷝᷞͫᷟᷠᷡͦͬᷣᷢᷤᷥͭͧͮͯᷦ̧̨̣̳͙̀́̂̃̄̆̇̈̉̊̋̍̎̿͜᷍᷎̅" \
             "̶̲̾͛̕᷏ᷓ᷐᷑᷒.;&ΘθꝋꝊ⁊ʼ≈∻ꝯꝮꜿꜾꝰꝝꝜꝭꝬꝸꝫꝪᚠᛘ℔^´`¨~¯˘˙" \
             "˚¸˛˜˝ˈ·‧․‥…:,჻∴∵∷⁖⁘|¦‖/⁄⫽\\⸌⸍⸜⸝_-‐‑⹀⸗‒–—―!¡?¿()⸦⸧⸨⸩[]{" \
             "}⁅⁆⟦⟧⸡⸠⸢⸣⸤⸥'′\"″‘’‚‛“”„‟‹«<⟨›>»⟩⸮⸪" \
             "⸫⸬⸭⋗              ​­#§*⁂@©®¬∧¶⁋✝†‡※⁜❦❧$¢£¤¥₰℈" \
             "℥+−±×÷=∞≠%‰°µ" \
             "←↑→↓▪▫•◌‣▹◃⏑⏒⏓⏔"

# these lists need to be updated as new punctuation and numbers are added to
# unicode

ORD_PUNCT_SYMBOL_TO_NONE = {33: None, 34: None, 35: None, 36: None, 37: None, 38: None, 39: None, 40: None, 41: None, 42: None, 43: None, 44: None, 45: None, 46: None, 47: None, 58: None, 59: None, 60: None, 61: None, 62: None, 63: None, 64: None, 91: None, 92: None, 93: None, 94: None, 95: None, 96: None, 123: None, 124: None, 125: None, 126: None, 161: None, 162: None, 163: None, 164: None, 165: None, 166: None, 167: None, 168: None, 169: None, 171: None, 172: None, 174: None, 175: None, 176: None, 177: None, 180: None, 182: None, 183: None, 184: None, 187: None, 191: None, 215: None, 247: None, 706: None, 707: None, 708: None, 709: None, 722: None, 723: None, 724: None, 725: None, 726: None, 727: None, 728: None, 729: None, 730: None, 731: None, 732: None, 733: None, 734: None, 735: None, 741: None, 742: None, 743: None, 744: None, 745: None, 746: None, 747: None, 749: None, 751: None, 752: None, 753: None, 754: None, 755: None, 756: None, 757: None, 758: None, 759: None, 760: None, 761: None, 762: None, 763: None, 764: None, 765: None, 766: None, 767: None, 885: None, 894: None, 900: None, 901: None, 903: None, 1014: None, 1154: None, 1370: None, 1371: None, 1372: None, 1373: None, 1374: None, 1375: None, 1417: None, 1418: None, 1421: None, 1422: None, 1423: None, 1470: None, 1472: None, 1475: None, 1478: None, 1523: None, 1524: None, 1542: None, 1543: None, 1544: None, 1545: None, 1546: None, 1547: None, 1548: None, 1549: None, 1550: None, 1551: None, 1563: None, 1566: None, 1567: None, 1642: None, 1643: None, 1644: None, 1645: None, 1748: None, 1758: None, 1769: None, 1789: None, 1790: None, 1792: None, 1793: None, 1794: None, 1795: None, 1796: None, 1797: None, 1798: None, 1799: None, 1800: None, 1801: None, 1802: None, 1803: None, 1804: None, 1805: None, 2038: None, 2039: None, 2040: None, 2041: None, 2046: None, 2047: None, 2096: None, 2097: None, 2098: None, 2099: None, 2100: None, 2101: None, 2102: None, 2103: None, 2104: None, 2105: None, 2106: None, 2107: None, 2108: None, 2109: None, 2110: None, 2142: None, 2404: None, 2405: None, 2416: None, 2546: None, 2547: None, 2554: None, 2555: None, 2557: None, 2678: None, 2800: None, 2801: None, 2928: None, 3059: None, 3060: None, 3061: None, 3062: None, 3063: None, 3064: None, 3065: None, 3066: None, 3199: None, 3204: None, 3407: None, 3449: None, 3572: None, 3647: None, 3663: None, 3674: None, 3675: None, 3841: None, 3842: None, 3843: None, 3844: None, 3845: None, 3846: None, 3847: None, 3848: None, 3849: None, 3850: None, 3851: None, 3852: None, 3853: None, 3854: None, 3855: None, 3856: None, 3857: None, 3858: None, 3859: None, 3860: None, 3861: None, 3862: None, 3863: None, 3866: None, 3867: None, 3868: None, 3869: None, 3870: None, 3871: None, 3892: None, 3894: None, 3896: None, 3898: None, 3899: None, 3900: None, 3901: None, 3973: None, 4030: None, 4031: None, 4032: None, 4033: None, 4034: None, 4035: None, 4036: None, 4037: None, 4039: None, 4040: None, 4041: None, 4042: None, 4043: None, 4044: None, 4046: None, 4047: None, 4048: None, 4049: None, 4050: None, 4051: None, 4052: None, 4053: None, 4054: None, 4055: None, 4056: None, 4057: None, 4058: None, 4170: None, 4171: None, 4172: None, 4173: None, 4174: None, 4175: None, 4254: None, 4255: None, 4347: None, 4960: None, 4961: None, 4962: None, 4963: None, 4964: None, 4965: None, 4966: None, 4967: None, 4968: None, 5008: None, 5009: None, 5010: None, 5011: None, 5012: None, 5013: None, 5014: None, 5015: None, 5016: None, 5017: None, 5120: None, 5741: None, 5742: None, 5787: None, 5788: None, 5867: None, 5868: None, 5869: None, 5941: None, 5942: None, 6100: None, 6101: None, 6102: None, 6104: None, 6105: None, 6106: None, 6107: None, 6144: None, 6145: None, 6146: None, 6147: None, 6148: None, 6149: None, 6150: None, 6151: None, 6152: None, 6153: None, 6154: None, 6464: None, 6468: None, 6469: None, 6622: None, 6623: None, 6624: None, 6625: None, 6626: None, 6627: None, 6628: None, 6629: None, 6630: None, 6631: None, 6632: None, 6633: None, 6634: None, 6635: None, 6636: None, 6637: None, 6638: None, 6639: None, 6640: None, 6641: None, 6642: None, 6643: None, 6644: None, 6645: None, 6646: None, 6647: None, 6648: None, 6649: None, 6650: None, 6651: None, 6652: None, 6653: None, 6654: None, 6655: None, 6686: None, 6687: None, 6816: None, 6817: None, 6818: None, 6819: None, 6820: None, 6821: None, 6822: None, 6824: None, 6825: None, 6826: None, 6827: None, 6828: None, 6829: None, 7002: None, 7003: None, 7004: None, 7005: None, 7006: None, 7007: None, 7008: None, 7009: None, 7010: None, 7011: None, 7012: None, 7013: None, 7014: None, 7015: None, 7016: None, 7017: None, 7018: None, 7028: None, 7029: None, 7030: None, 7031: None, 7032: None, 7033: None, 7034: None, 7035: None, 7036: None, 7164: None, 7165: None, 7166: None, 7167: None, 7227: None, 7228: None, 7229: None, 7230: None, 7231: None, 7294: None, 7295: None, 7360: None, 7361: None, 7362: None, 7363: None, 7364: None, 7365: None, 7366: None, 7367: None, 7379: None, 8125: None, 8127: None, 8128: None, 8129: None, 8141: None, 8142: None, 8143: None, 8157: None, 8158: None, 8159: None, 8173: None, 8174: None, 8175: None, 8189: None, 8190: None, 8208: None, 8209: None, 8210: None, 8211: None, 8212: None, 8213: None, 8214: None, 8215: None, 8216: None, 8217: None, 8218: None, 8219: None, 8220: None, 8221: None, 8222: None, 8223: None, 8224: None, 8225: None, 8226: None, 8227: None, 8228: None, 8229: None, 8230: None, 8231: None, 8240: None, 8241: None, 8242: None, 8243: None, 8244: None, 8245: None, 8246: None, 8247: None, 8248: None, 8249: None, 8250: None, 8251: None, 8252: None, 8253: None, 8254: None, 8255: None, 8256: None, 8257: None, 8258: None, 8259: None, 8260: None, 8261: None, 8262: None, 8263: None, 8264: None, 8265: None, 8266: None, 8267: None, 8268: None, 8269: None, 8270: None, 8271: None, 8272: None, 8273: None, 8274: None, 8275: None, 8276: None, 8277: None, 8278: None, 8279: None, 8280: None, 8281: None, 8282: None, 8283: None, 8284: None, 8285: None, 8286: None, 8314: None, 8315: None, 8316: None, 8317: None, 8318: None, 8330: None, 8331: None, 8332: None, 8333: None, 8334: None, 8352: None, 8353: None, 8354: None, 8355: None, 8356: None, 8357: None, 8358: None, 8359: None, 8360: None, 8361: None, 8362: None, 8363: None, 8364: None, 8365: None, 8366: None, 8367: None, 8368: None, 8369: None, 8370: None, 8371: None, 8372: None, 8373: None, 8374: None, 8375: None, 8376: None, 8377: None, 8378: None, 8379: None, 8380: None, 8381: None, 8382: None, 8383: None, 8448: None, 8449: None, 8451: None, 8452: None, 8453: None, 8454: None, 8456: None, 8457: None, 8468: None, 8470: None, 8471: None, 8472: None, 8478: None, 8479: None, 8480: None, 8481: None, 8482: None, 8483: None, 8485: None, 8487: None, 8489: None, 8494: None, 8506: None, 8507: None, 8512: None, 8513: None, 8514: None, 8515: None, 8516: None, 8522: None, 8523: None, 8524: None, 8525: None, 8527: None, 8586: None, 8587: None, 8592: None, 8593: None, 8594: None, 8595: None, 8596: None, 8597: None, 8598: None, 8599: None, 8600: None, 8601: None, 8602: None, 8603: None, 8604: None, 8605: None, 8606: None, 8607: None, 8608: None, 8609: None, 8610: None, 8611: None, 8612: None, 8613: None, 8614: None, 8615: None, 8616: None, 8617: None, 8618: None, 8619: None, 8620: None, 8621: None, 8622: None, 8623: None, 8624: None, 8625: None, 8626: None, 8627: None, 8628: None, 8629: None, 8630: None, 8631: None, 8632: None, 8633: None, 8634: None, 8635: None, 8636: None, 8637: None, 8638: None, 8639: None, 8640: None, 8641: None, 8642: None, 8643: None, 8644: None, 8645: None, 8646: None, 8647: None, 8648: None, 8649: None, 8650: None, 8651: None, 8652: None, 8653: None, 8654: None, 8655: None, 8656: None, 8657: None, 8658: None, 8659: None, 8660: None, 8661: None, 8662: None, 8663: None, 8664: None, 8665: None, 8666: None, 8667: None, 8668: None, 8669: None, 8670: None, 8671: None, 8672: None, 8673: None, 8674: None, 8675: None, 8676: None, 8677: None, 8678: None, 8679: None, 8680: None, 8681: None, 8682: None, 8683: None, 8684: None, 8685: None, 8686: None, 8687: None, 8688: None, 8689: None, 8690: None, 8691: None, 8692: None, 8693: None, 8694: None, 8695: None, 8696: None, 8697: None, 8698: None, 8699: None, 8700: None, 8701: None, 8702: None, 8703: None, 8704: None, 8705: None, 8706: None, 8707: None, 8708: None, 8709: None, 8710: None, 8711: None, 8712: None, 8713: None, 8714: None, 8715: None, 8716: None, 8717: None, 8718: None, 8719: None, 8720: None, 8721: None, 8722: None, 8723: None, 8724: None, 8725: None, 8726: None, 8727: None, 8728: None, 8729: None, 8730: None, 8731: None, 8732: None, 8733: None, 8734: None, 8735: None, 8736: None, 8737: None, 8738: None, 8739: None, 8740: None, 8741: None, 8742: None, 8743: None, 8744: None, 8745: None, 8746: None, 8747: None, 8748: None, 8749: None, 8750: None, 8751: None, 8752: None, 8753: None, 8754: None, 8755: None, 8756: None, 8757: None, 8758: None, 8759: None, 8760: None, 8761: None, 8762: None, 8763: None, 8764: None, 8765: None, 8766: None, 8767: None, 8768: None, 8769: None, 8770: None, 8771: None, 8772: None, 8773: None, 8774: None, 8775: None, 8776: None, 8777: None, 8778: None, 8779: None, 8780: None, 8781: None, 8782: None, 8783: None, 8784: None, 8785: None, 8786: None, 8787: None, 8788: None, 8789: None, 8790: None, 8791: None, 8792: None, 8793: None, 8794: None, 8795: None, 8796: None, 8797: None, 8798: None, 8799: None, 8800: None, 8801: None, 8802: None, 8803: None, 8804: None, 8805: None, 8806: None, 8807: None, 8808: None, 8809: None, 8810: None, 8811: None, 8812: None, 8813: None, 8814: None, 8815: None, 8816: None, 8817: None, 8818: None, 8819: None, 8820: None, 8821: None, 8822: None, 8823: None, 8824: None, 8825: None, 8826: None, 8827: None, 8828: None, 8829: None, 8830: None, 8831: None, 8832: None, 8833: None, 8834: None, 8835: None, 8836: None, 8837: None, 8838: None, 8839: None, 8840: None, 8841: None, 8842: None, 8843: None, 8844: None, 8845: None, 8846: None, 8847: None, 8848: None, 8849: None, 8850: None, 8851: None, 8852: None, 8853: None, 8854: None, 8855: None, 8856: None, 8857: None, 8858: None, 8859: None, 8860: None, 8861: None, 8862: None, 8863: None, 8864: None, 8865: None, 8866: None, 8867: None, 8868: None, 8869: None, 8870: None, 8871: None, 8872: None, 8873: None, 8874: None, 8875: None, 8876: None, 8877: None, 8878: None, 8879: None, 8880: None, 8881: None, 8882: None, 8883: None, 8884: None, 8885: None, 8886: None, 8887: None, 8888: None, 8889: None, 8890: None, 8891: None, 8892: None, 8893: None, 8894: None, 8895: None, 8896: None, 8897: None, 8898: None, 8899: None, 8900: None, 8901: None, 8902: None, 8903: None, 8904: None, 8905: None, 8906: None, 8907: None, 8908: None, 8909: None, 8910: None, 8911: None, 8912: None, 8913: None, 8914: None, 8915: None, 8916: None, 8917: None, 8918: None, 8919: None, 8920: None, 8921: None, 8922: None, 8923: None, 8924: None, 8925: None, 8926: None, 8927: None, 8928: None, 8929: None, 8930: None, 8931: None, 8932: None, 8933: None, 8934: None, 8935: None, 8936: None, 8937: None, 8938: None, 8939: None, 8940: None, 8941: None, 8942: None, 8943: None, 8944: None, 8945: None, 8946: None, 8947: None, 8948: None, 8949: None, 8950: None, 8951: None, 8952: None, 8953: None, 8954: None, 8955: None, 8956: None, 8957: None, 8958: None, 8959: None, 8960: None, 8961: None, 8962: None, 8963: None, 8964: None, 8965: None, 8966: None, 8967: None, 8968: None, 8969: None, 8970: None, 8971: None, 8972: None, 8973: None, 8974: None, 8975: None, 8976: None, 8977: None, 8978: None, 8979: None, 8980: None, 8981: None, 8982: None, 8983: None, 8984: None, 8985: None, 8986: None, 8987: None, 8988: None, 8989: None, 8990: None, 8991: None, 8992: None, 8993: None, 8994: None, 8995: None, 8996: None, 8997: None, 8998: None, 8999: None, 9000: None, 9001: None, 9002: None, 9003: None, 9004: None, 9005: None, 9006: None, 9007: None, 9008: None, 9009: None, 9010: None, 9011: None, 9012: None, 9013: None, 9014: None, 9015: None, 9016: None, 9017: None, 9018: None, 9019: None, 9020: None, 9021: None, 9022: None, 9023: None, 9024: None, 9025: None, 9026: None, 9027: None, 9028: None, 9029: None, 9030: None, 9031: None, 9032: None, 9033: None, 9034: None, 9035: None, 9036: None, 9037: None, 9038: None, 9039: None, 9040: None, 9041: None, 9042: None, 9043: None, 9044: None, 9045: None, 9046: None, 9047: None, 9048: None, 9049: None, 9050: None, 9051: None, 9052: None, 9053: None, 9054: None, 9055: None, 9056: None, 9057: None, 9058: None, 9059: None, 9060: None, 9061: None, 9062: None, 9063: None, 9064: None, 9065: None, 9066: None, 9067: None, 9068: None, 9069: None, 9070: None, 9071: None, 9072: None, 9073: None, 9074: None, 9075: None, 9076: None, 9077: None, 9078: None, 9079: None, 9080: None, 9081: None, 9082: None, 9083: None, 9084: None, 9085: None, 9086: None, 9087: None, 9088: None, 9089: None, 9090: None, 9091: None, 9092: None, 9093: None, 9094: None, 9095: None, 9096: None, 9097: None, 9098: None, 9099: None, 9100: None, 9101: None, 9102: None, 9103: None, 9104: None, 9105: None, 9106: None, 9107: None, 9108: None, 9109: None, 9110: None, 9111: None, 9112: None, 9113: None, 9114: None, 9115: None, 9116: None, 9117: None, 9118: None, 9119: None, 9120: None, 9121: None, 9122: None, 9123: None, 9124: None, 9125: None, 9126: None, 9127: None, 9128: None, 9129: None, 9130: None, 9131: None, 9132: None, 9133: None, 9134: None, 9135: None, 9136: None, 9137: None, 9138: None, 9139: None, 9140: None, 9141: None, 9142: None, 9143: None, 9144: None, 9145: None, 9146: None, 9147: None, 9148: None, 9149: None, 9150: None, 9151: None, 9152: None, 9153: None, 9154: None, 9155: None, 9156: None, 9157: None, 9158: None, 9159: None, 9160: None, 9161: None, 9162: None, 9163: None, 9164: None, 9165: None, 9166: None, 9167: None, 9168: None, 9169: None, 9170: None, 9171: None, 9172: None, 9173: None, 9174: None, 9175: None, 9176: None, 9177: None, 9178: None, 9179: None, 9180: None, 9181: None, 9182: None, 9183: None, 9184: None, 9185: None, 9186: None, 9187: None, 9188: None, 9189: None, 9190: None, 9191: None, 9192: None, 9193: None, 9194: None, 9195: None, 9196: None, 9197: None, 9198: None, 9199: None, 9200: None, 9201: None, 9202: None, 9203: None, 9204: None, 9205: None, 9206: None, 9207: None, 9208: None, 9209: None, 9210: None, 9211: None, 9212: None, 9213: None, 9214: None, 9215: None, 9216: None, 9217: None, 9218: None, 9219: None, 9220: None, 9221: None, 9222: None, 9223: None, 9224: None, 9225: None, 9226: None, 9227: None, 9228: None, 9229: None, 9230: None, 9231: None, 9232: None, 9233: None, 9234: None, 9235: None, 9236: None, 9237: None, 9238: None, 9239: None, 9240: None, 9241: None, 9242: None, 9243: None, 9244: None, 9245: None, 9246: None, 9247: None, 9248: None, 9249: None, 9250: None, 9251: None, 9252: None, 9253: None, 9254: None, 9280: None, 9281: None, 9282: None, 9283: None, 9284: None, 9285: None, 9286: None, 9287: None, 9288: None, 9289: None, 9290: None, 9372: None, 9373: None, 9374: None, 9375: None, 9376: None, 9377: None, 9378: None, 9379: None, 9380: None, 9381: None, 9382: None, 9383: None, 9384: None, 9385: None, 9386: None, 9387: None, 9388: None, 9389: None, 9390: None, 9391: None, 9392: None, 9393: None, 9394: None, 9395: None, 9396: None, 9397: None, 9398: None, 9399: None, 9400: None, 9401: None, 9402: None, 9403: None, 9404: None, 9405: None, 9406: None, 9407: None, 9408: None, 9409: None, 9410: None, 9411: None, 9412: None, 9413: None, 9414: None, 9415: None, 9416: None, 9417: None, 9418: None, 9419: None, 9420: None, 9421: None, 9422: None, 9423: None, 9424: None, 9425: None, 9426: None, 9427: None, 9428: None, 9429: None, 9430: None, 9431: None, 9432: None, 9433: None, 9434: None, 9435: None, 9436: None, 9437: None, 9438: None, 9439: None, 9440: None, 9441: None, 9442: None, 9443: None, 9444: None, 9445: None, 9446: None, 9447: None, 9448: None, 9449: None, 9472: None, 9473: None, 9474: None, 9475: None, 9476: None, 9477: None, 9478: None, 9479: None, 9480: None, 9481: None, 9482: None, 9483: None, 9484: None, 9485: None, 9486: None, 9487: None, 9488: None, 9489: None, 9490: None, 9491: None, 9492: None, 9493: None, 9494: None, 9495: None, 9496: None, 9497: None, 9498: None, 9499: None, 9500: None, 9501: None, 9502: None, 9503: None, 9504: None, 9505: None, 9506: None, 9507: None, 9508: None, 9509: None, 9510: None, 9511: None, 9512: None, 9513: None, 9514: None, 9515: None, 9516: None, 9517: None, 9518: None, 9519: None, 9520: None, 9521: None, 9522: None, 9523: None, 9524: None, 9525: None, 9526: None, 9527: None, 9528: None, 9529: None, 9530: None, 9531: None, 9532: None, 9533: None, 9534: None, 9535: None, 9536: None, 9537: None, 9538: None, 9539: None, 9540: None, 9541: None, 9542: None, 9543: None, 9544: None, 9545: None, 9546: None, 9547: None, 9548: None, 9549: None, 9550: None, 9551: None, 9552: None, 9553: None, 9554: None, 9555: None, 9556: None, 9557: None, 9558: None, 9559: None, 9560: None, 9561: None, 9562: None, 9563: None, 9564: None, 9565: None, 9566: None, 9567: None, 9568: None, 9569: None, 9570: None, 9571: None, 9572: None, 9573: None, 9574: None, 9575: None, 9576: None, 9577: None, 9578: None, 9579: None, 9580: None, 9581: None, 9582: None, 9583: None, 9584: None, 9585: None, 9586: None, 9587: None, 9588: None, 9589: None, 9590: None, 9591: None, 9592: None, 9593: None, 9594: None, 9595: None, 9596: None, 9597: None, 9598: None, 9599: None, 9600: None, 9601: None, 9602: None, 9603: None, 9604: None, 9605: None, 9606: None, 9607: None, 9608: None, 9609: None, 9610: None, 9611: None, 9612: None, 9613: None, 9614: None, 9615: None, 9616: None, 9617: None, 9618: None, 9619: None, 9620: None, 9621: None, 9622: None, 9623: None, 9624: None, 9625: None, 9626: None, 9627: None, 9628: None, 9629: None, 9630: None, 9631: None, 9632: None, 9633: None, 9634: None, 9635: None, 9636: None, 9637: None, 9638: None, 9639: None, 9640: None, 9641: None, 9642: None, 9643: None, 9644: None, 9645: None, 9646: None, 9647: None, 9648: None, 9649: None, 9650: None, 9651: None, 9652: None, 9653: None, 9654: None, 9655: None, 9656: None, 9657: None, 9658: None, 9659: None, 9660: None, 9661: None, 9662: None, 9663: None, 9664: None, 9665: None, 9666: None, 9667: None, 9668: None, 9669: None, 9670: None, 9671: None, 9672: None, 9673: None, 9674: None, 9675: None, 9676: None, 9677: None, 9678: None, 9679: None, 9680: None, 9681: None, 9682: None, 9683: None, 9684: None, 9685: None, 9686: None, 9687: None, 9688: None, 9689: None, 9690: None, 9691: None, 9692: None, 9693: None, 9694: None, 9695: None, 9696: None, 9697: None, 9698: None, 9699: None, 9700: None, 9701: None, 9702: None, 9703: None, 9704: None, 9705: None, 9706: None, 9707: None, 9708: None, 9709: None, 9710: None, 9711: None, 9712: None, 9713: None, 9714: None, 9715: None, 9716: None, 9717: None, 9718: None, 9719: None, 9720: None, 9721: None, 9722: None, 9723: None, 9724: None, 9725: None, 9726: None, 9727: None, 9728: None, 9729: None, 9730: None, 9731: None, 9732: None, 9733: None, 9734: None, 9735: None, 9736: None, 9737: None, 9738: None, 9739: None, 9740: None, 9741: None, 9742: None, 9743: None, 9744: None, 9745: None, 9746: None, 9747: None, 9748: None, 9749: None, 9750: None, 9751: None, 9752: None, 9753: None, 9754: None, 9755: None, 9756: None, 9757: None, 9758: None, 9759: None, 9760: None, 9761: None, 9762: None, 9763: None, 9764: None, 9765: None, 9766: None, 9767: None, 9768: None, 9769: None, 9770: None, 9771: None, 9772: None, 9773: None, 9774: None, 9775: None, 9776: None, 9777: None, 9778: None, 9779: None, 9780: None, 9781: None, 9782: None, 9783: None, 9784: None, 9785: None, 9786: None, 9787: None, 9788: None, 9789: None, 9790: None, 9791: None, 9792: None, 9793: None, 9794: None, 9795: None, 9796: None, 9797: None, 9798: None, 9799: None, 9800: None, 9801: None, 9802: None, 9803: None, 9804: None, 9805: None, 9806: None, 9807: None, 9808: None, 9809: None, 9810: None, 9811: None, 9812: None, 9813: None, 9814: None, 9815: None, 9816: None, 9817: None, 9818: None, 9819: None, 9820: None, 9821: None, 9822: None, 9823: None, 9824: None, 9825: None, 9826: None, 9827: None, 9828: None, 9829: None, 9830: None, 9831: None, 9832: None, 9833: None, 9834: None, 9835: None, 9836: None, 9837: None, 9838: None, 9839: None, 9840: None, 9841: None, 9842: None, 9843: None, 9844: None, 9845: None, 9846: None, 9847: None, 9848: None, 9849: None, 9850: None, 9851: None, 9852: None, 9853: None, 9854: None, 9855: None, 9856: None, 9857: None, 9858: None, 9859: None, 9860: None, 9861: None, 9862: None, 9863: None, 9864: None, 9865: None, 9866: None, 9867: None, 9868: None, 9869: None, 9870: None, 9871: None, 9872: None, 9873: None, 9874: None, 9875: None, 9876: None, 9877: None, 9878: None, 9879: None, 9880: None, 9881: None, 9882: None, 9883: None, 9884: None, 9885: None, 9886: None, 9887: None, 9888: None, 9889: None, 9890: None, 9891: None, 9892: None, 9893: None, 9894: None, 9895: None, 9896: None, 9897: None, 9898: None, 9899: None, 9900: None, 9901: None, 9902: None, 9903: None, 9904: None, 9905: None, 9906: None, 9907: None, 9908: None, 9909: None, 9910: None, 9911: None, 9912: None, 9913: None, 9914: None, 9915: None, 9916: None, 9917: None, 9918: None, 9919: None, 9920: None, 9921: None, 9922: None, 9923: None, 9924: None, 9925: None, 9926: None, 9927: None, 9928: None, 9929: None, 9930: None, 9931: None, 9932: None, 9933: None, 9934: None, 9935: None, 9936: None, 9937: None, 9938: None, 9939: None, 9940: None, 9941: None, 9942: None, 9943: None, 9944: None, 9945: None, 9946: None, 9947: None, 9948: None, 9949: None, 9950: None, 9951: None, 9952: None, 9953: None, 9954: None, 9955: None, 9956: None, 9957: None, 9958: None, 9959: None, 9960: None, 9961: None, 9962: None, 9963: None, 9964: None, 9965: None, 9966: None, 9967: None, 9968: None, 9969: None, 9970: None, 9971: None, 9972: None, 9973: None, 9974: None, 9975: None, 9976: None, 9977: None, 9978: None, 9979: None, 9980: None, 9981: None, 9982: None, 9983: None, 9984: None, 9985: None, 9986: None, 9987: None, 9988: None, 9989: None, 9990: None, 9991: None, 9992: None, 9993: None, 9994: None, 9995: None, 9996: None, 9997: None, 9998: None, 9999: None, 10000: None, 10001: None, 10002: None, 10003: None, 10004: None, 10005: None, 10006: None, 10007: None, 10008: None, 10009: None, 10010: None, 10011: None, 10012: None, 10013: None, 10014: None, 10015: None, 10016: None, 10017: None, 10018: None, 10019: None, 10020: None, 10021: None, 10022: None, 10023: None, 10024: None, 10025: None, 10026: None, 10027: None, 10028: None, 10029: None, 10030: None, 10031: None, 10032: None, 10033: None, 10034: None, 10035: None, 10036: None, 10037: None, 10038: None, 10039: None, 10040: None, 10041: None, 10042: None, 10043: None, 10044: None, 10045: None, 10046: None, 10047: None, 10048: None, 10049: None, 10050: None, 10051: None, 10052: None, 10053: None, 10054: None, 10055: None, 10056: None, 10057: None, 10058: None, 10059: None, 10060: None, 10061: None, 10062: None, 10063: None, 10064: None, 10065: None, 10066: None, 10067: None, 10068: None, 10069: None, 10070: None, 10071: None, 10072: None, 10073: None, 10074: None, 10075: None, 10076: None, 10077: None, 10078: None, 10079: None, 10080: None, 10081: None, 10082: None, 10083: None, 10084: None, 10085: None, 10086: None, 10087: None, 10088: None, 10089: None, 10090: None, 10091: None, 10092: None, 10093: None, 10094: None, 10095: None, 10096: None, 10097: None, 10098: None, 10099: None, 10100: None, 10101: None, 10132: None, 10133: None, 10134: None, 10135: None, 10136: None, 10137: None, 10138: None, 10139: None, 10140: None, 10141: None, 10142: None, 10143: None, 10144: None, 10145: None, 10146: None, 10147: None, 10148: None, 10149: None, 10150: None, 10151: None, 10152: None, 10153: None, 10154: None, 10155: None, 10156: None, 10157: None, 10158: None, 10159: None, 10160: None, 10161: None, 10162: None, 10163: None, 10164: None, 10165: None, 10166: None, 10167: None, 10168: None, 10169: None, 10170: None, 10171: None, 10172: None, 10173: None, 10174: None, 10175: None, 10176: None, 10177: None, 10178: None, 10179: None, 10180: None, 10181: None, 10182: None, 10183: None, 10184: None, 10185: None, 10186: None, 10187: None, 10188: None, 10189: None, 10190: None, 10191: None, 10192: None, 10193: None, 10194: None, 10195: None, 10196: None, 10197: None, 10198: None, 10199: None, 10200: None, 10201: None, 10202: None, 10203: None, 10204: None, 10205: None, 10206: None, 10207: None, 10208: None, 10209: None, 10210: None, 10211: None, 10212: None, 10213: None, 10214: None, 10215: None, 10216: None, 10217: None, 10218: None, 10219: None, 10220: None, 10221: None, 10222: None, 10223: None, 10224: None, 10225: None, 10226: None, 10227: None, 10228: None, 10229: None, 10230: None, 10231: None, 10232: None, 10233: None, 10234: None, 10235: None, 10236: None, 10237: None, 10238: None, 10239: None, 10240: None, 10241: None, 10242: None, 10243: None, 10244: None, 10245: None, 10246: None, 10247: None, 10248: None, 10249: None, 10250: None, 10251: None, 10252: None, 10253: None, 10254: None, 10255: None, 10256: None, 10257: None, 10258: None, 10259: None, 10260: None, 10261: None, 10262: None, 10263: None, 10264: None, 10265: None, 10266: None, 10267: None, 10268: None, 10269: None, 10270: None, 10271: None, 10272: None, 10273: None, 10274: None, 10275: None, 10276: None, 10277: None, 10278: None, 10279: None, 10280: None, 10281: None, 10282: None, 10283: None, 10284: None, 10285: None, 10286: None, 10287: None, 10288: None, 10289: None, 10290: None, 10291: None, 10292: None, 10293: None, 10294: None, 10295: None, 10296: None, 10297: None, 10298: None, 10299: None, 10300: None, 10301: None, 10302: None, 10303: None, 10304: None, 10305: None, 10306: None, 10307: None, 10308: None, 10309: None, 10310: None, 10311: None, 10312: None, 10313: None, 10314: None, 10315: None, 10316: None, 10317: None, 10318: None, 10319: None, 10320: None, 10321: None, 10322: None, 10323: None, 10324: None, 10325: None, 10326: None, 10327: None, 10328: None, 10329: None, 10330: None, 10331: None, 10332: None, 10333: None, 10334: None, 10335: None, 10336: None, 10337: None, 10338: None, 10339: None, 10340: None, 10341: None, 10342: None, 10343: None, 10344: None, 10345: None, 10346: None, 10347: None, 10348: None, 10349: None, 10350: None, 10351: None, 10352: None, 10353: None, 10354: None, 10355: None, 10356: None, 10357: None, 10358: None, 10359: None, 10360: None, 10361: None, 10362: None, 10363: None, 10364: None, 10365: None, 10366: None, 10367: None, 10368: None, 10369: None, 10370: None, 10371: None, 10372: None, 10373: None, 10374: None, 10375: None, 10376: None, 10377: None, 10378: None, 10379: None, 10380: None, 10381: None, 10382: None, 10383: None, 10384: None, 10385: None, 10386: None, 10387: None, 10388: None, 10389: None, 10390: None, 10391: None, 10392: None, 10393: None, 10394: None, 10395: None, 10396: None, 10397: None, 10398: None, 10399: None, 10400: None, 10401: None, 10402: None, 10403: None, 10404: None, 10405: None, 10406: None, 10407: None, 10408: None, 10409: None, 10410: None, 10411: None, 10412: None, 10413: None, 10414: None, 10415: None, 10416: None, 10417: None, 10418: None, 10419: None, 10420: None, 10421: None, 10422: None, 10423: None, 10424: None, 10425: None, 10426: None, 10427: None, 10428: None, 10429: None, 10430: None, 10431: None, 10432: None, 10433: None, 10434: None, 10435: None, 10436: None, 10437: None, 10438: None, 10439: None, 10440: None, 10441: None, 10442: None, 10443: None, 10444: None, 10445: None, 10446: None, 10447: None, 10448: None, 10449: None, 10450: None, 10451: None, 10452: None, 10453: None, 10454: None, 10455: None, 10456: None, 10457: None, 10458: None, 10459: None, 10460: None, 10461: None, 10462: None, 10463: None, 10464: None, 10465: None, 10466: None, 10467: None, 10468: None, 10469: None, 10470: None, 10471: None, 10472: None, 10473: None, 10474: None, 10475: None, 10476: None, 10477: None, 10478: None, 10479: None, 10480: None, 10481: None, 10482: None, 10483: None, 10484: None, 10485: None, 10486: None, 10487: None, 10488: None, 10489: None, 10490: None, 10491: None, 10492: None, 10493: None, 10494: None, 10495: None, 10496: None, 10497: None, 10498: None, 10499: None, 10500: None, 10501: None, 10502: None, 10503: None, 10504: None, 10505: None, 10506: None, 10507: None, 10508: None, 10509: None, 10510: None, 10511: None, 10512: None, 10513: None, 10514: None, 10515: None, 10516: None, 10517: None, 10518: None, 10519: None, 10520: None, 10521: None, 10522: None, 10523: None, 10524: None, 10525: None, 10526: None, 10527: None, 10528: None, 10529: None, 10530: None, 10531: None, 10532: None, 10533: None, 10534: None, 10535: None, 10536: None, 10537: None, 10538: None, 10539: None, 10540: None, 10541: None, 10542: None, 10543: None, 10544: None, 10545: None, 10546: None, 10547: None, 10548: None, 10549: None, 10550: None, 10551: None, 10552: None, 10553: None, 10554: None, 10555: None, 10556: None, 10557: None, 10558: None, 10559: None, 10560: None, 10561: None, 10562: None, 10563: None, 10564: None, 10565: None, 10566: None, 10567: None, 10568: None, 10569: None, 10570: None, 10571: None, 10572: None, 10573: None, 10574: None, 10575: None, 10576: None, 10577: None, 10578: None, 10579: None, 10580: None, 10581: None, 10582: None, 10583: None, 10584: None, 10585: None, 10586: None, 10587: None, 10588: None, 10589: None, 10590: None, 10591: None, 10592: None, 10593: None, 10594: None, 10595: None, 10596: None, 10597: None, 10598: None, 10599: None, 10600: None, 10601: None, 10602: None, 10603: None, 10604: None, 10605: None, 10606: None, 10607: None, 10608: None, 10609: None, 10610: None, 10611: None, 10612: None, 10613: None, 10614: None, 10615: None, 10616: None, 10617: None, 10618: None, 10619: None, 10620: None, 10621: None, 10622: None, 10623: None, 10624: None, 10625: None, 10626: None, 10627: None, 10628: None, 10629: None, 10630: None, 10631: None, 10632: None, 10633: None, 10634: None, 10635: None, 10636: None, 10637: None, 10638: None, 10639: None, 10640: None, 10641: None, 10642: None, 10643: None, 10644: None, 10645: None, 10646: None, 10647: None, 10648: None, 10649: None, 10650: None, 10651: None, 10652: None, 10653: None, 10654: None, 10655: None, 10656: None, 10657: None, 10658: None, 10659: None, 10660: None, 10661: None, 10662: None, 10663: None, 10664: None, 10665: None, 10666: None, 10667: None, 10668: None, 10669: None, 10670: None, 10671: None, 10672: None, 10673: None, 10674: None, 10675: None, 10676: None, 10677: None, 10678: None, 10679: None, 10680: None, 10681: None, 10682: None, 10683: None, 10684: None, 10685: None, 10686: None, 10687: None, 10688: None, 10689: None, 10690: None, 10691: None, 10692: None, 10693: None, 10694: None, 10695: None, 10696: None, 10697: None, 10698: None, 10699: None, 10700: None, 10701: None, 10702: None, 10703: None, 10704: None, 10705: None, 10706: None, 10707: None, 10708: None, 10709: None, 10710: None, 10711: None, 10712: None, 10713: None, 10714: None, 10715: None, 10716: None, 10717: None, 10718: None, 10719: None, 10720: None, 10721: None, 10722: None, 10723: None, 10724: None, 10725: None, 10726: None, 10727: None, 10728: None, 10729: None, 10730: None, 10731: None, 10732: None, 10733: None, 10734: None, 10735: None, 10736: None, 10737: None, 10738: None, 10739: None, 10740: None, 10741: None, 10742: None, 10743: None, 10744: None, 10745: None, 10746: None, 10747: None, 10748: None, 10749: None, 10750: None, 10751: None, 10752: None, 10753: None, 10754: None, 10755: None, 10756: None, 10757: None, 10758: None, 10759: None, 10760: None, 10761: None, 10762: None, 10763: None, 10764: None, 10765: None, 10766: None, 10767: None, 10768: None, 10769: None, 10770: None, 10771: None, 10772: None, 10773: None, 10774: None, 10775: None, 10776: None, 10777: None, 10778: None, 10779: None, 10780: None, 10781: None, 10782: None, 10783: None, 10784: None, 10785: None, 10786: None, 10787: None, 10788: None, 10789: None, 10790: None, 10791: None, 10792: None, 10793: None, 10794: None, 10795: None, 10796: None, 10797: None, 10798: None, 10799: None, 10800: None, 10801: None, 10802: None, 10803: None, 10804: None, 10805: None, 10806: None, 10807: None, 10808: None, 10809: None, 10810: None, 10811: None, 10812: None, 10813: None, 10814: None, 10815: None, 10816: None, 10817: None, 10818: None, 10819: None, 10820: None, 10821: None, 10822: None, 10823: None, 10824: None, 10825: None, 10826: None, 10827: None, 10828: None, 10829: None, 10830: None, 10831: None, 10832: None, 10833: None, 10834: None, 10835: None, 10836: None, 10837: None, 10838: None, 10839: None, 10840: None, 10841: None, 10842: None, 10843: None, 10844: None, 10845: None, 10846: None, 10847: None, 10848: None, 10849: None, 10850: None, 10851: None, 10852: None, 10853: None, 10854: None, 10855: None, 10856: None, 10857: None, 10858: None, 10859: None, 10860: None, 10861: None, 10862: None, 10863: None, 10864: None, 10865: None, 10866: None, 10867: None, 10868: None, 10869: None, 10870: None, 10871: None, 10872: None, 10873: None, 10874: None, 10875: None, 10876: None, 10877: None, 10878: None, 10879: None, 10880: None, 10881: None, 10882: None, 10883: None, 10884: None, 10885: None, 10886: None, 10887: None, 10888: None, 10889: None, 10890: None, 10891: None, 10892: None, 10893: None, 10894: None, 10895: None, 10896: None, 10897: None, 10898: None, 10899: None, 10900: None, 10901: None, 10902: None, 10903: None, 10904: None, 10905: None, 10906: None, 10907: None, 10908: None, 10909: None, 10910: None, 10911: None, 10912: None, 10913: None, 10914: None, 10915: None, 10916: None, 10917: None, 10918: None, 10919: None, 10920: None, 10921: None, 10922: None, 10923: None, 10924: None, 10925: None, 10926: None, 10927: None, 10928: None, 10929: None, 10930: None, 10931: None, 10932: None, 10933: None, 10934: None, 10935: None, 10936: None, 10937: None, 10938: None, 10939: None, 10940: None, 10941: None, 10942: None, 10943: None, 10944: None, 10945: None, 10946: None, 10947: None, 10948: None, 10949: None, 10950: None, 10951: None, 10952: None, 10953: None, 10954: None, 10955: None, 10956: None, 10957: None, 10958: None, 10959: None, 10960: None, 10961: None, 10962: None, 10963: None, 10964: None, 10965: None, 10966: None, 10967: None, 10968: None, 10969: None, 10970: None, 10971: None, 10972: None, 10973: None, 10974: None, 10975: None, 10976: None, 10977: None, 10978: None, 10979: None, 10980: None, 10981: None, 10982: None, 10983: None, 10984: None, 10985: None, 10986: None, 10987: None, 10988: None, 10989: None, 10990: None, 10991: None, 10992: None, 10993: None, 10994: None, 10995: None, 10996: None, 10997: None, 10998: None, 10999: None, 11000: None, 11001: None, 11002: None, 11003: None, 11004: None, 11005: None, 11006: None, 11007: None, 11008: None, 11009: None, 11010: None, 11011: None, 11012: None, 11013: None, 11014: None, 11015: None, 11016: None, 11017: None, 11018: None, 11019: None, 11020: None, 11021: None, 11022: None, 11023: None, 11024: None, 11025: None, 11026: None, 11027: None, 11028: None, 11029: None, 11030: None, 11031: None, 11032: None, 11033: None, 11034: None, 11035: None, 11036: None, 11037: None, 11038: None, 11039: None, 11040: None, 11041: None, 11042: None, 11043: None, 11044: None, 11045: None, 11046: None, 11047: None, 11048: None, 11049: None, 11050: None, 11051: None, 11052: None, 11053: None, 11054: None, 11055: None, 11056: None, 11057: None, 11058: None, 11059: None, 11060: None, 11061: None, 11062: None, 11063: None, 11064: None, 11065: None, 11066: None, 11067: None, 11068: None, 11069: None, 11070: None, 11071: None, 11072: None, 11073: None, 11074: None, 11075: None, 11076: None, 11077: None, 11078: None, 11079: None, 11080: None, 11081: None, 11082: None, 11083: None, 11084: None, 11085: None, 11086: None, 11087: None, 11088: None, 11089: None, 11090: None, 11091: None, 11092: None, 11093: None, 11094: None, 11095: None, 11096: None, 11097: None, 11098: None, 11099: None, 11100: None, 11101: None, 11102: None, 11103: None, 11104: None, 11105: None, 11106: None, 11107: None, 11108: None, 11109: None, 11110: None, 11111: None, 11112: None, 11113: None, 11114: None, 11115: None, 11116: None, 11117: None, 11118: None, 11119: None, 11120: None, 11121: None, 11122: None, 11123: None, 11126: None, 11127: None, 11128: None, 11129: None, 11130: None, 11131: None, 11132: None, 11133: None, 11134: None, 11135: None, 11136: None, 11137: None, 11138: None, 11139: None, 11140: None, 11141: None, 11142: None, 11143: None, 11144: None, 11145: None, 11146: None, 11147: None, 11148: None, 11149: None, 11150: None, 11151: None, 11152: None, 11153: None, 11154: None, 11155: None, 11156: None, 11157: None, 11160: None, 11161: None, 11162: None, 11163: None, 11164: None, 11165: None, 11166: None, 11167: None, 11168: None, 11169: None, 11170: None, 11171: None, 11172: None, 11173: None, 11174: None, 11175: None, 11176: None, 11177: None, 11178: None, 11179: None, 11180: None, 11181: None, 11182: None, 11183: None, 11184: None, 11185: None, 11186: None, 11187: None, 11188: None, 11189: None, 11190: None, 11191: None, 11192: None, 11193: None, 11194: None, 11195: None, 11196: None, 11197: None, 11198: None, 11199: None, 11200: None, 11201: None, 11202: None, 11203: None, 11204: None, 11205: None, 11206: None, 11207: None, 11208: None, 11210: None, 11211: None, 11212: None, 11213: None, 11214: None, 11215: None, 11216: None, 11217: None, 11218: None, 11219: None, 11220: None, 11221: None, 11222: None, 11223: None, 11224: None, 11225: None, 11226: None, 11227: None, 11228: None, 11229: None, 11230: None, 11231: None, 11232: None, 11233: None, 11234: None, 11235: None, 11236: None, 11237: None, 11238: None, 11239: None, 11240: None, 11241: None, 11242: None, 11243: None, 11244: None, 11245: None, 11246: None, 11247: None, 11248: None, 11249: None, 11250: None, 11251: None, 11252: None, 11253: None, 11254: None, 11255: None, 11256: None, 11257: None, 11258: None, 11259: None, 11260: None, 11261: None, 11262: None, 11493: None, 11494: None, 11495: None, 11496: None, 11497: None, 11498: None, 11513: None, 11514: None, 11515: None, 11516: None, 11518: None, 11519: None, 11632: None, 11776: None, 11777: None, 11778: None, 11779: None, 11780: None, 11781: None, 11782: None, 11783: None, 11784: None, 11785: None, 11786: None, 11787: None, 11788: None, 11789: None, 11790: None, 11791: None, 11792: None, 11793: None, 11794: None, 11795: None, 11796: None, 11797: None, 11798: None, 11799: None, 11800: None, 11801: None, 11802: None, 11803: None, 11804: None, 11805: None, 11806: None, 11807: None, 11808: None, 11809: None, 11810: None, 11811: None, 11812: None, 11813: None, 11814: None, 11815: None, 11816: None, 11817: None, 11818: None, 11819: None, 11820: None, 11821: None, 11822: None, 11824: None, 11825: None, 11826: None, 11827: None, 11828: None, 11829: None, 11830: None, 11831: None, 11832: None, 11833: None, 11834: None, 11835: None, 11836: None, 11837: None, 11838: None, 11839: None, 11840: None, 11841: None, 11842: None, 11843: None, 11844: None, 11845: None, 11846: None, 11847: None, 11848: None, 11849: None, 11850: None, 11851: None, 11852: None, 11853: None, 11854: None, 11904: None, 11905: None, 11906: None, 11907: None, 11908: None, 11909: None, 11910: None, 11911: None, 11912: None, 11913: None, 11914: None, 11915: None, 11916: None, 11917: None, 11918: None, 11919: None, 11920: None, 11921: None, 11922: None, 11923: None, 11924: None, 11925: None, 11926: None, 11927: None, 11928: None, 11929: None, 11931: None, 11932: None, 11933: None, 11934: None, 11935: None, 11936: None, 11937: None, 11938: None, 11939: None, 11940: None, 11941: None, 11942: None, 11943: None, 11944: None, 11945: None, 11946: None, 11947: None, 11948: None, 11949: None, 11950: None, 11951: None, 11952: None, 11953: None, 11954: None, 11955: None, 11956: None, 11957: None, 11958: None, 11959: None, 11960: None, 11961: None, 11962: None, 11963: None, 11964: None, 11965: None, 11966: None, 11967: None, 11968: None, 11969: None, 11970: None, 11971: None, 11972: None, 11973: None, 11974: None, 11975: None, 11976: None, 11977: None, 11978: None, 11979: None, 11980: None, 11981: None, 11982: None, 11983: None, 11984: None, 11985: None, 11986: None, 11987: None, 11988: None, 11989: None, 11990: None, 11991: None, 11992: None, 11993: None, 11994: None, 11995: None, 11996: None, 11997: None, 11998: None, 11999: None, 12000: None, 12001: None, 12002: None, 12003: None, 12004: None, 12005: None, 12006: None, 12007: None, 12008: None, 12009: None, 12010: None, 12011: None, 12012: None, 12013: None, 12014: None, 12015: None, 12016: None, 12017: None, 12018: None, 12019: None, 12032: None, 12033: None, 12034: None, 12035: None, 12036: None, 12037: None, 12038: None, 12039: None, 12040: None, 12041: None, 12042: None, 12043: None, 12044: None, 12045: None, 12046: None, 12047: None, 12048: None, 12049: None, 12050: None, 12051: None, 12052: None, 12053: None, 12054: None, 12055: None, 12056: None, 12057: None, 12058: None, 12059: None, 12060: None, 12061: None, 12062: None, 12063: None, 12064: None, 12065: None, 12066: None, 12067: None, 12068: None, 12069: None, 12070: None, 12071: None, 12072: None, 12073: None, 12074: None, 12075: None, 12076: None, 12077: None, 12078: None, 12079: None, 12080: None, 12081: None, 12082: None, 12083: None, 12084: None, 12085: None, 12086: None, 12087: None, 12088: None, 12089: None, 12090: None, 12091: None, 12092: None, 12093: None, 12094: None, 12095: None, 12096: None, 12097: None, 12098: None, 12099: None, 12100: None, 12101: None, 12102: None, 12103: None, 12104: None, 12105: None, 12106: None, 12107: None, 12108: None, 12109: None, 12110: None, 12111: None, 12112: None, 12113: None, 12114: None, 12115: None, 12116: None, 12117: None, 12118: None, 12119: None, 12120: None, 12121: None, 12122: None, 12123: None, 12124: None, 12125: None, 12126: None, 12127: None, 12128: None, 12129: None, 12130: None, 12131: None, 12132: None, 12133: None, 12134: None, 12135: None, 12136: None, 12137: None, 12138: None, 12139: None, 12140: None, 12141: None, 12142: None, 12143: None, 12144: None, 12145: None, 12146: None, 12147: None, 12148: None, 12149: None, 12150: None, 12151: None, 12152: None, 12153: None, 12154: None, 12155: None, 12156: None, 12157: None, 12158: None, 12159: None, 12160: None, 12161: None, 12162: None, 12163: None, 12164: None, 12165: None, 12166: None, 12167: None, 12168: None, 12169: None, 12170: None, 12171: None, 12172: None, 12173: None, 12174: None, 12175: None, 12176: None, 12177: None, 12178: None, 12179: None, 12180: None, 12181: None, 12182: None, 12183: None, 12184: None, 12185: None, 12186: None, 12187: None, 12188: None, 12189: None, 12190: None, 12191: None, 12192: None, 12193: None, 12194: None, 12195: None, 12196: None, 12197: None, 12198: None, 12199: None, 12200: None, 12201: None, 12202: None, 12203: None, 12204: None, 12205: None, 12206: None, 12207: None, 12208: None, 12209: None, 12210: None, 12211: None, 12212: None, 12213: None, 12214: None, 12215: None, 12216: None, 12217: None, 12218: None, 12219: None, 12220: None, 12221: None, 12222: None, 12223: None, 12224: None, 12225: None, 12226: None, 12227: None, 12228: None, 12229: None, 12230: None, 12231: None, 12232: None, 12233: None, 12234: None, 12235: None, 12236: None, 12237: None, 12238: None, 12239: None, 12240: None, 12241: None, 12242: None, 12243: None, 12244: None, 12245: None, 12272: None, 12273: None, 12274: None, 12275: None, 12276: None, 12277: None, 12278: None, 12279: None, 12280: None, 12281: None, 12282: None, 12283: None, 12289: None, 12290: None, 12291: None, 12292: None, 12296: None, 12297: None, 12298: None, 12299: None, 12300: None, 12301: None, 12302: None, 12303: None, 12304: None, 12305: None, 12306: None, 12307: None, 12308: None, 12309: None, 12310: None, 12311: None, 12312: None, 12313: None, 12314: None, 12315: None, 12316: None, 12317: None, 12318: None, 12319: None, 12320: None, 12336: None, 12342: None, 12343: None, 12349: None, 12350: None, 12351: None, 12443: None, 12444: None, 12448: None, 12539: None, 12688: None, 12689: None, 12694: None, 12695: None, 12696: None, 12697: None, 12698: None, 12699: None, 12700: None, 12701: None, 12702: None, 12703: None, 12736: None, 12737: None, 12738: None, 12739: None, 12740: None, 12741: None, 12742: None, 12743: None, 12744: None, 12745: None, 12746: None, 12747: None, 12748: None, 12749: None, 12750: None, 12751: None, 12752: None, 12753: None, 12754: None, 12755: None, 12756: None, 12757: None, 12758: None, 12759: None, 12760: None, 12761: None, 12762: None, 12763: None, 12764: None, 12765: None, 12766: None, 12767: None, 12768: None, 12769: None, 12770: None, 12771: None, 12800: None, 12801: None, 12802: None, 12803: None, 12804: None, 12805: None, 12806: None, 12807: None, 12808: None, 12809: None, 12810: None, 12811: None, 12812: None, 12813: None, 12814: None, 12815: None, 12816: None, 12817: None, 12818: None, 12819: None, 12820: None, 12821: None, 12822: None, 12823: None, 12824: None, 12825: None, 12826: None, 12827: None, 12828: None, 12829: None, 12830: None, 12842: None, 12843: None, 12844: None, 12845: None, 12846: None, 12847: None, 12848: None, 12849: None, 12850: None, 12851: None, 12852: None, 12853: None, 12854: None, 12855: None, 12856: None, 12857: None, 12858: None, 12859: None, 12860: None, 12861: None, 12862: None, 12863: None, 12864: None, 12865: None, 12866: None, 12867: None, 12868: None, 12869: None, 12870: None, 12871: None, 12880: None, 12896: None, 12897: None, 12898: None, 12899: None, 12900: None, 12901: None, 12902: None, 12903: None, 12904: None, 12905: None, 12906: None, 12907: None, 12908: None, 12909: None, 12910: None, 12911: None, 12912: None, 12913: None, 12914: None, 12915: None, 12916: None, 12917: None, 12918: None, 12919: None, 12920: None, 12921: None, 12922: None, 12923: None, 12924: None, 12925: None, 12926: None, 12927: None, 12938: None, 12939: None, 12940: None, 12941: None, 12942: None, 12943: None, 12944: None, 12945: None, 12946: None, 12947: None, 12948: None, 12949: None, 12950: None, 12951: None, 12952: None, 12953: None, 12954: None, 12955: None, 12956: None, 12957: None, 12958: None, 12959: None, 12960: None, 12961: None, 12962: None, 12963: None, 12964: None, 12965: None, 12966: None, 12967: None, 12968: None, 12969: None, 12970: None, 12971: None, 12972: None, 12973: None, 12974: None, 12975: None, 12976: None, 12992: None, 12993: None, 12994: None, 12995: None, 12996: None, 12997: None, 12998: None, 12999: None, 13000: None, 13001: None, 13002: None, 13003: None, 13004: None, 13005: None, 13006: None, 13007: None, 13008: None, 13009: None, 13010: None, 13011: None, 13012: None, 13013: None, 13014: None, 13015: None, 13016: None, 13017: None, 13018: None, 13019: None, 13020: None, 13021: None, 13022: None, 13023: None, 13024: None, 13025: None, 13026: None, 13027: None, 13028: None, 13029: None, 13030: None, 13031: None, 13032: None, 13033: None, 13034: None, 13035: None, 13036: None, 13037: None, 13038: None, 13039: None, 13040: None, 13041: None, 13042: None, 13043: None, 13044: None, 13045: None, 13046: None, 13047: None, 13048: None, 13049: None, 13050: None, 13051: None, 13052: None, 13053: None, 13054: None, 13056: None, 13057: None, 13058: None, 13059: None, 13060: None, 13061: None, 13062: None, 13063: None, 13064: None, 13065: None, 13066: None, 13067: None, 13068: None, 13069: None, 13070: None, 13071: None, 13072: None, 13073: None, 13074: None, 13075: None, 13076: None, 13077: None, 13078: None, 13079: None, 13080: None, 13081: None, 13082: None, 13083: None, 13084: None, 13085: None, 13086: None, 13087: None, 13088: None, 13089: None, 13090: None, 13091: None, 13092: None, 13093: None, 13094: None, 13095: None, 13096: None, 13097: None, 13098: None, 13099: None, 13100: None, 13101: None, 13102: None, 13103: None, 13104: None, 13105: None, 13106: None, 13107: None, 13108: None, 13109: None, 13110: None, 13111: None, 13112: None, 13113: None, 13114: None, 13115: None, 13116: None, 13117: None, 13118: None, 13119: None, 13120: None, 13121: None, 13122: None, 13123: None, 13124: None, 13125: None, 13126: None, 13127: None, 13128: None, 13129: None, 13130: None, 13131: None, 13132: None, 13133: None, 13134: None, 13135: None, 13136: None, 13137: None, 13138: None, 13139: None, 13140: None, 13141: None, 13142: None, 13143: None, 13144: None, 13145: None, 13146: None, 13147: None, 13148: None, 13149: None, 13150: None, 13151: None, 13152: None, 13153: None, 13154: None, 13155: None, 13156: None, 13157: None, 13158: None, 13159: None, 13160: None, 13161: None, 13162: None, 13163: None, 13164: None, 13165: None, 13166: None, 13167: None, 13168: None, 13169: None, 13170: None, 13171: None, 13172: None, 13173: None, 13174: None, 13175: None, 13176: None, 13177: None, 13178: None, 13179: None, 13180: None, 13181: None, 13182: None, 13183: None, 13184: None, 13185: None, 13186: None, 13187: None, 13188: None, 13189: None, 13190: None, 13191: None, 13192: None, 13193: None, 13194: None, 13195: None, 13196: None, 13197: None, 13198: None, 13199: None, 13200: None, 13201: None, 13202: None, 13203: None, 13204: None, 13205: None, 13206: None, 13207: None, 13208: None, 13209: None, 13210: None, 13211: None, 13212: None, 13213: None, 13214: None, 13215: None, 13216: None, 13217: None, 13218: None, 13219: None, 13220: None, 13221: None, 13222: None, 13223: None, 13224: None, 13225: None, 13226: None, 13227: None, 13228: None, 13229: None, 13230: None, 13231: None, 13232: None, 13233: None, 13234: None, 13235: None, 13236: None, 13237: None, 13238: None, 13239: None, 13240: None, 13241: None, 13242: None, 13243: None, 13244: None, 13245: None, 13246: None, 13247: None, 13248: None, 13249: None, 13250: None, 13251: None, 13252: None, 13253: None, 13254: None, 13255: None, 13256: None, 13257: None, 13258: None, 13259: None, 13260: None, 13261: None, 13262: None, 13263: None, 13264: None, 13265: None, 13266: None, 13267: None, 13268: None, 13269: None, 13270: None, 13271: None, 13272: None, 13273: None, 13274: None, 13275: None, 13276: None, 13277: None, 13278: None, 13279: None, 13280: None, 13281: None, 13282: None, 13283: None, 13284: None, 13285: None, 13286: None, 13287: None, 13288: None, 13289: None, 13290: None, 13291: None, 13292: None, 13293: None, 13294: None, 13295: None, 13296: None, 13297: None, 13298: None, 13299: None, 13300: None, 13301: None, 13302: None, 13303: None, 13304: None, 13305: None, 13306: None, 13307: None, 13308: None, 13309: None, 13310: None, 13311: None, 19904: None, 19905: None, 19906: None, 19907: None, 19908: None, 19909: None, 19910: None, 19911: None, 19912: None, 19913: None, 19914: None, 19915: None, 19916: None, 19917: None, 19918: None, 19919: None, 19920: None, 19921: None, 19922: None, 19923: None, 19924: None, 19925: None, 19926: None, 19927: None, 19928: None, 19929: None, 19930: None, 19931: None, 19932: None, 19933: None, 19934: None, 19935: None, 19936: None, 19937: None, 19938: None, 19939: None, 19940: None, 19941: None, 19942: None, 19943: None, 19944: None, 19945: None, 19946: None, 19947: None, 19948: None, 19949: None, 19950: None, 19951: None, 19952: None, 19953: None, 19954: None, 19955: None, 19956: None, 19957: None, 19958: None, 19959: None, 19960: None, 19961: None, 19962: None, 19963: None, 19964: None, 19965: None, 19966: None, 19967: None, 42128: None, 42129: None, 42130: None, 42131: None, 42132: None, 42133: None, 42134: None, 42135: None, 42136: None, 42137: None, 42138: None, 42139: None, 42140: None, 42141: None, 42142: None, 42143: None, 42144: None, 42145: None, 42146: None, 42147: None, 42148: None, 42149: None, 42150: None, 42151: None, 42152: None, 42153: None, 42154: None, 42155: None, 42156: None, 42157: None, 42158: None, 42159: None, 42160: None, 42161: None, 42162: None, 42163: None, 42164: None, 42165: None, 42166: None, 42167: None, 42168: None, 42169: None, 42170: None, 42171: None, 42172: None, 42173: None, 42174: None, 42175: None, 42176: None, 42177: None, 42178: None, 42179: None, 42180: None, 42181: None, 42182: None, 42238: None, 42239: None, 42509: None, 42510: None, 42511: None, 42611: None, 42622: None, 42738: None, 42739: None, 42740: None, 42741: None, 42742: None, 42743: None, 42752: None, 42753: None, 42754: None, 42755: None, 42756: None, 42757: None, 42758: None, 42759: None, 42760: None, 42761: None, 42762: None, 42763: None, 42764: None, 42765: None, 42766: None, 42767: None, 42768: None, 42769: None, 42770: None, 42771: None, 42772: None, 42773: None, 42774: None, 42784: None, 42785: None, 42889: None, 42890: None, 43048: None, 43049: None, 43050: None, 43051: None, 43062: None, 43063: None, 43064: None, 43065: None, 43124: None, 43125: None, 43126: None, 43127: None, 43214: None, 43215: None, 43256: None, 43257: None, 43258: None, 43260: None, 43310: None, 43311: None, 43359: None, 43457: None, 43458: None, 43459: None, 43460: None, 43461: None, 43462: None, 43463: None, 43464: None, 43465: None, 43466: None, 43467: None, 43468: None, 43469: None, 43486: None, 43487: None, 43612: None, 43613: None, 43614: None, 43615: None, 43639: None, 43640: None, 43641: None, 43742: None, 43743: None, 43760: None, 43761: None, 43867: None, 44011: None, 64297: None, 64434: None, 64435: None, 64436: None, 64437: None, 64438: None, 64439: None, 64440: None, 64441: None, 64442: None, 64443: None, 64444: None, 64445: None, 64446: None, 64447: None, 64448: None, 64449: None, 64830: None, 64831: None, 65020: None, 65021: None, 65040: None, 65041: None, 65042: None, 65043: None, 65044: None, 65045: None, 65046: None, 65047: None, 65048: None, 65049: None, 65072: None, 65073: None, 65074: None, 65075: None, 65076: None, 65077: None, 65078: None, 65079: None, 65080: None, 65081: None, 65082: None, 65083: None, 65084: None, 65085: None, 65086: None, 65087: None, 65088: None, 65089: None, 65090: None, 65091: None, 65092: None, 65093: None, 65094: None, 65095: None, 65096: None, 65097: None, 65098: None, 65099: None, 65100: None, 65101: None, 65102: None, 65103: None, 65104: None, 65105: None, 65106: None, 65108: None, 65109: None, 65110: None, 65111: None, 65112: None, 65113: None, 65114: None, 65115: None, 65116: None, 65117: None, 65118: None, 65119: None, 65120: None, 65121: None, 65122: None, 65123: None, 65124: None, 65125: None, 65126: None, 65128: None, 65129: None, 65130: None, 65131: None, 65281: None, 65282: None, 65283: None, 65284: None, 65285: None, 65286: None, 65287: None, 65288: None, 65289: None, 65290: None, 65291: None, 65292: None, 65293: None, 65294: None, 65295: None, 65306: None, 65307: None, 65308: None, 65309: None, 65310: None, 65311: None, 65312: None, 65339: None, 65340: None, 65341: None, 65342: None, 65343: None, 65344: None, 65371: None, 65372: None, 65373: None, 65374: None, 65375: None, 65376: None, 65377: None, 65378: None, 65379: None, 65380: None, 65381: None, 65504: None, 65505: None, 65506: None, 65507: None, 65508: None, 65509: None, 65510: None, 65512: None, 65513: None, 65514: None, 65515: None, 65516: None, 65517: None, 65518: None, 65532: None, 65533: None, 65792: None, 65793: None, 65794: None, 65847: None, 65848: None, 65849: None, 65850: None, 65851: None, 65852: None, 65853: None, 65854: None, 65855: None, 65913: None, 65914: None, 65915: None, 65916: None, 65917: None, 65918: None, 65919: None, 65920: None, 65921: None, 65922: None, 65923: None, 65924: None, 65925: None, 65926: None, 65927: None, 65928: None, 65929: None, 65932: None, 65933: None, 65934: None, 65936: None, 65937: None, 65938: None, 65939: None, 65940: None, 65941: None, 65942: None, 65943: None, 65944: None, 65945: None, 65946: None, 65947: None, 65952: None, 66000: None, 66001: None, 66002: None, 66003: None, 66004: None, 66005: None, 66006: None, 66007: None, 66008: None, 66009: None, 66010: None, 66011: None, 66012: None, 66013: None, 66014: None, 66015: None, 66016: None, 66017: None, 66018: None, 66019: None, 66020: None, 66021: None, 66022: None, 66023: None, 66024: None, 66025: None, 66026: None, 66027: None, 66028: None, 66029: None, 66030: None, 66031: None, 66032: None, 66033: None, 66034: None, 66035: None, 66036: None, 66037: None, 66038: None, 66039: None, 66040: None, 66041: None, 66042: None, 66043: None, 66044: None, 66463: None, 66512: None, 66927: None, 67671: None, 67703: None, 67704: None, 67871: None, 67903: None, 68176: None, 68177: None, 68178: None, 68179: None, 68180: None, 68181: None, 68182: None, 68183: None, 68184: None, 68223: None, 68296: None, 68336: None, 68337: None, 68338: None, 68339: None, 68340: None, 68341: None, 68342: None, 68409: None, 68410: None, 68411: None, 68412: None, 68413: None, 68414: None, 68415: None, 68505: None, 68506: None, 68507: None, 68508: None, 69461: None, 69462: None, 69463: None, 69464: None, 69465: None, 69703: None, 69704: None, 69705: None, 69706: None, 69707: None, 69708: None, 69709: None, 69819: None, 69820: None, 69822: None, 69823: None, 69824: None, 69825: None, 69952: None, 69953: None, 69954: None, 69955: None, 70004: None, 70005: None, 70085: None, 70086: None, 70087: None, 70088: None, 70093: None, 70107: None, 70109: None, 70110: None, 70111: None, 70200: None, 70201: None, 70202: None, 70203: None, 70204: None, 70205: None, 70313: None, 70731: None, 70732: None, 70733: None, 70734: None, 70735: None, 70747: None, 70749: None, 70854: None, 71105: None, 71106: None, 71107: None, 71108: None, 71109: None, 71110: None, 71111: None, 71112: None, 71113: None, 71114: None, 71115: None, 71116: None, 71117: None, 71118: None, 71119: None, 71120: None, 71121: None, 71122: None, 71123: None, 71124: None, 71125: None, 71126: None, 71127: None, 71233: None, 71234: None, 71235: None, 71264: None, 71265: None, 71266: None, 71267: None, 71268: None, 71269: None, 71270: None, 71271: None, 71272: None, 71273: None, 71274: None, 71275: None, 71276: None, 71484: None, 71485: None, 71486: None, 71487: None, 71739: None, 72255: None, 72256: None, 72257: None, 72258: None, 72259: None, 72260: None, 72261: None, 72262: None, 72346: None, 72347: None, 72348: None, 72350: None, 72351: None, 72352: None, 72353: None, 72354: None, 72769: None, 72770: None, 72771: None, 72772: None, 72773: None, 72816: None, 72817: None, 73463: None, 73464: None, 74864: None, 74865: None, 74866: None, 74867: None, 74868: None, 92782: None, 92783: None, 92917: None, 92983: None, 92984: None, 92985: None, 92986: None, 92987: None, 92988: None, 92989: None, 92990: None, 92991: None, 92996: None, 92997: None, 93847: None, 93848: None, 93849: None, 93850: None, 113820: None, 113823: None, 118784: None, 118785: None, 118786: None, 118787: None, 118788: None, 118789: None, 118790: None, 118791: None, 118792: None, 118793: None, 118794: None, 118795: None, 118796: None, 118797: None, 118798: None, 118799: None, 118800: None, 118801: None, 118802: None, 118803: None, 118804: None, 118805: None, 118806: None, 118807: None, 118808: None, 118809: None, 118810: None, 118811: None, 118812: None, 118813: None, 118814: None, 118815: None, 118816: None, 118817: None, 118818: None, 118819: None, 118820: None, 118821: None, 118822: None, 118823: None, 118824: None, 118825: None, 118826: None, 118827: None, 118828: None, 118829: None, 118830: None, 118831: None, 118832: None, 118833: None, 118834: None, 118835: None, 118836: None, 118837: None, 118838: None, 118839: None, 118840: None, 118841: None, 118842: None, 118843: None, 118844: None, 118845: None, 118846: None, 118847: None, 118848: None, 118849: None, 118850: None, 118851: None, 118852: None, 118853: None, 118854: None, 118855: None, 118856: None, 118857: None, 118858: None, 118859: None, 118860: None, 118861: None, 118862: None, 118863: None, 118864: None, 118865: None, 118866: None, 118867: None, 118868: None, 118869: None, 118870: None, 118871: None, 118872: None, 118873: None, 118874: None, 118875: None, 118876: None, 118877: None, 118878: None, 118879: None, 118880: None, 118881: None, 118882: None, 118883: None, 118884: None, 118885: None, 118886: None, 118887: None, 118888: None, 118889: None, 118890: None, 118891: None, 118892: None, 118893: None, 118894: None, 118895: None, 118896: None, 118897: None, 118898: None, 118899: None, 118900: None, 118901: None, 118902: None, 118903: None, 118904: None, 118905: None, 118906: None, 118907: None, 118908: None, 118909: None, 118910: None, 118911: None, 118912: None, 118913: None, 118914: None, 118915: None, 118916: None, 118917: None, 118918: None, 118919: None, 118920: None, 118921: None, 118922: None, 118923: None, 118924: None, 118925: None, 118926: None, 118927: None, 118928: None, 118929: None, 118930: None, 118931: None, 118932: None, 118933: None, 118934: None, 118935: None, 118936: None, 118937: None, 118938: None, 118939: None, 118940: None, 118941: None, 118942: None, 118943: None, 118944: None, 118945: None, 118946: None, 118947: None, 118948: None, 118949: None, 118950: None, 118951: None, 118952: None, 118953: None, 118954: None, 118955: None, 118956: None, 118957: None, 118958: None, 118959: None, 118960: None, 118961: None, 118962: None, 118963: None, 118964: None, 118965: None, 118966: None, 118967: None, 118968: None, 118969: None, 118970: None, 118971: None, 118972: None, 118973: None, 118974: None, 118975: None, 118976: None, 118977: None, 118978: None, 118979: None, 118980: None, 118981: None, 118982: None, 118983: None, 118984: None, 118985: None, 118986: None, 118987: None, 118988: None, 118989: None, 118990: None, 118991: None, 118992: None, 118993: None, 118994: None, 118995: None, 118996: None, 118997: None, 118998: None, 118999: None, 119000: None, 119001: None, 119002: None, 119003: None, 119004: None, 119005: None, 119006: None, 119007: None, 119008: None, 119009: None, 119010: None, 119011: None, 119012: None, 119013: None, 119014: None, 119015: None, 119016: None, 119017: None, 119018: None, 119019: None, 119020: None, 119021: None, 119022: None, 119023: None, 119024: None, 119025: None, 119026: None, 119027: None, 119028: None, 119029: None, 119040: None, 119041: None, 119042: None, 119043: None, 119044: None, 119045: None, 119046: None, 119047: None, 119048: None, 119049: None, 119050: None, 119051: None, 119052: None, 119053: None, 119054: None, 119055: None, 119056: None, 119057: None, 119058: None, 119059: None, 119060: None, 119061: None, 119062: None, 119063: None, 119064: None, 119065: None, 119066: None, 119067: None, 119068: None, 119069: None, 119070: None, 119071: None, 119072: None, 119073: None, 119074: None, 119075: None, 119076: None, 119077: None, 119078: None, 119081: None, 119082: None, 119083: None, 119084: None, 119085: None, 119086: None, 119087: None, 119088: None, 119089: None, 119090: None, 119091: None, 119092: None, 119093: None, 119094: None, 119095: None, 119096: None, 119097: None, 119098: None, 119099: None, 119100: None, 119101: None, 119102: None, 119103: None, 119104: None, 119105: None, 119106: None, 119107: None, 119108: None, 119109: None, 119110: None, 119111: None, 119112: None, 119113: None, 119114: None, 119115: None, 119116: None, 119117: None, 119118: None, 119119: None, 119120: None, 119121: None, 119122: None, 119123: None, 119124: None, 119125: None, 119126: None, 119127: None, 119128: None, 119129: None, 119130: None, 119131: None, 119132: None, 119133: None, 119134: None, 119135: None, 119136: None, 119137: None, 119138: None, 119139: None, 119140: None, 119146: None, 119147: None, 119148: None, 119171: None, 119172: None, 119180: None, 119181: None, 119182: None, 119183: None, 119184: None, 119185: None, 119186: None, 119187: None, 119188: None, 119189: None, 119190: None, 119191: None, 119192: None, 119193: None, 119194: None, 119195: None, 119196: None, 119197: None, 119198: None, 119199: None, 119200: None, 119201: None, 119202: None, 119203: None, 119204: None, 119205: None, 119206: None, 119207: None, 119208: None, 119209: None, 119214: None, 119215: None, 119216: None, 119217: None, 119218: None, 119219: None, 119220: None, 119221: None, 119222: None, 119223: None, 119224: None, 119225: None, 119226: None, 119227: None, 119228: None, 119229: None, 119230: None, 119231: None, 119232: None, 119233: None, 119234: None, 119235: None, 119236: None, 119237: None, 119238: None, 119239: None, 119240: None, 119241: None, 119242: None, 119243: None, 119244: None, 119245: None, 119246: None, 119247: None, 119248: None, 119249: None, 119250: None, 119251: None, 119252: None, 119253: None, 119254: None, 119255: None, 119256: None, 119257: None, 119258: None, 119259: None, 119260: None, 119261: None, 119262: None, 119263: None, 119264: None, 119265: None, 119266: None, 119267: None, 119268: None, 119269: None, 119270: None, 119271: None, 119272: None, 119296: None, 119297: None, 119298: None, 119299: None, 119300: None, 119301: None, 119302: None, 119303: None, 119304: None, 119305: None, 119306: None, 119307: None, 119308: None, 119309: None, 119310: None, 119311: None, 119312: None, 119313: None, 119314: None, 119315: None, 119316: None, 119317: None, 119318: None, 119319: None, 119320: None, 119321: None, 119322: None, 119323: None, 119324: None, 119325: None, 119326: None, 119327: None, 119328: None, 119329: None, 119330: None, 119331: None, 119332: None, 119333: None, 119334: None, 119335: None, 119336: None, 119337: None, 119338: None, 119339: None, 119340: None, 119341: None, 119342: None, 119343: None, 119344: None, 119345: None, 119346: None, 119347: None, 119348: None, 119349: None, 119350: None, 119351: None, 119352: None, 119353: None, 119354: None, 119355: None, 119356: None, 119357: None, 119358: None, 119359: None, 119360: None, 119361: None, 119365: None, 119552: None, 119553: None, 119554: None, 119555: None, 119556: None, 119557: None, 119558: None, 119559: None, 119560: None, 119561: None, 119562: None, 119563: None, 119564: None, 119565: None, 119566: None, 119567: None, 119568: None, 119569: None, 119570: None, 119571: None, 119572: None, 119573: None, 119574: None, 119575: None, 119576: None, 119577: None, 119578: None, 119579: None, 119580: None, 119581: None, 119582: None, 119583: None, 119584: None, 119585: None, 119586: None, 119587: None, 119588: None, 119589: None, 119590: None, 119591: None, 119592: None, 119593: None, 119594: None, 119595: None, 119596: None, 119597: None, 119598: None, 119599: None, 119600: None, 119601: None, 119602: None, 119603: None, 119604: None, 119605: None, 119606: None, 119607: None, 119608: None, 119609: None, 119610: None, 119611: None, 119612: None, 119613: None, 119614: None, 119615: None, 119616: None, 119617: None, 119618: None, 119619: None, 119620: None, 119621: None, 119622: None, 119623: None, 119624: None, 119625: None, 119626: None, 119627: None, 119628: None, 119629: None, 119630: None, 119631: None, 119632: None, 119633: None, 119634: None, 119635: None, 119636: None, 119637: None, 119638: None, 120513: None, 120539: None, 120571: None, 120597: None, 120629: None, 120655: None, 120687: None, 120713: None, 120745: None, 120771: None, 120832: None, 120833: None, 120834: None, 120835: None, 120836: None, 120837: None, 120838: None, 120839: None, 120840: None, 120841: None, 120842: None, 120843: None, 120844: None, 120845: None, 120846: None, 120847: None, 120848: None, 120849: None, 120850: None, 120851: None, 120852: None, 120853: None, 120854: None, 120855: None, 120856: None, 120857: None, 120858: None, 120859: None, 120860: None, 120861: None, 120862: None, 120863: None, 120864: None, 120865: None, 120866: None, 120867: None, 120868: None, 120869: None, 120870: None, 120871: None, 120872: None, 120873: None, 120874: None, 120875: None, 120876: None, 120877: None, 120878: None, 120879: None, 120880: None, 120881: None, 120882: None, 120883: None, 120884: None, 120885: None, 120886: None, 120887: None, 120888: None, 120889: None, 120890: None, 120891: None, 120892: None, 120893: None, 120894: None, 120895: None, 120896: None, 120897: None, 120898: None, 120899: None, 120900: None, 120901: None, 120902: None, 120903: None, 120904: None, 120905: None, 120906: None, 120907: None, 120908: None, 120909: None, 120910: None, 120911: None, 120912: None, 120913: None, 120914: None, 120915: None, 120916: None, 120917: None, 120918: None, 120919: None, 120920: None, 120921: None, 120922: None, 120923: None, 120924: None, 120925: None, 120926: None, 120927: None, 120928: None, 120929: None, 120930: None, 120931: None, 120932: None, 120933: None, 120934: None, 120935: None, 120936: None, 120937: None, 120938: None, 120939: None, 120940: None, 120941: None, 120942: None, 120943: None, 120944: None, 120945: None, 120946: None, 120947: None, 120948: None, 120949: None, 120950: None, 120951: None, 120952: None, 120953: None, 120954: None, 120955: None, 120956: None, 120957: None, 120958: None, 120959: None, 120960: None, 120961: None, 120962: None, 120963: None, 120964: None, 120965: None, 120966: None, 120967: None, 120968: None, 120969: None, 120970: None, 120971: None, 120972: None, 120973: None, 120974: None, 120975: None, 120976: None, 120977: None, 120978: None, 120979: None, 120980: None, 120981: None, 120982: None, 120983: None, 120984: None, 120985: None, 120986: None, 120987: None, 120988: None, 120989: None, 120990: None, 120991: None, 120992: None, 120993: None, 120994: None, 120995: None, 120996: None, 120997: None, 120998: None, 120999: None, 121000: None, 121001: None, 121002: None, 121003: None, 121004: None, 121005: None, 121006: None, 121007: None, 121008: None, 121009: None, 121010: None, 121011: None, 121012: None, 121013: None, 121014: None, 121015: None, 121016: None, 121017: None, 121018: None, 121019: None, 121020: None, 121021: None, 121022: None, 121023: None, 121024: None, 121025: None, 121026: None, 121027: None, 121028: None, 121029: None, 121030: None, 121031: None, 121032: None, 121033: None, 121034: None, 121035: None, 121036: None, 121037: None, 121038: None, 121039: None, 121040: None, 121041: None, 121042: None, 121043: None, 121044: None, 121045: None, 121046: None, 121047: None, 121048: None, 121049: None, 121050: None, 121051: None, 121052: None, 121053: None, 121054: None, 121055: None, 121056: None, 121057: None, 121058: None, 121059: None, 121060: None, 121061: None, 121062: None, 121063: None, 121064: None, 121065: None, 121066: None, 121067: None, 121068: None, 121069: None, 121070: None, 121071: None, 121072: None, 121073: None, 121074: None, 121075: None, 121076: None, 121077: None, 121078: None, 121079: None, 121080: None, 121081: None, 121082: None, 121083: None, 121084: None, 121085: None, 121086: None, 121087: None, 121088: None, 121089: None, 121090: None, 121091: None, 121092: None, 121093: None, 121094: None, 121095: None, 121096: None, 121097: None, 121098: None, 121099: None, 121100: None, 121101: None, 121102: None, 121103: None, 121104: None, 121105: None, 121106: None, 121107: None, 121108: None, 121109: None, 121110: None, 121111: None, 121112: None, 121113: None, 121114: None, 121115: None, 121116: None, 121117: None, 121118: None, 121119: None, 121120: None, 121121: None, 121122: None, 121123: None, 121124: None, 121125: None, 121126: None, 121127: None, 121128: None, 121129: None, 121130: None, 121131: None, 121132: None, 121133: None, 121134: None, 121135: None, 121136: None, 121137: None, 121138: None, 121139: None, 121140: None, 121141: None, 121142: None, 121143: None, 121144: None, 121145: None, 121146: None, 121147: None, 121148: None, 121149: None, 121150: None, 121151: None, 121152: None, 121153: None, 121154: None, 121155: None, 121156: None, 121157: None, 121158: None, 121159: None, 121160: None, 121161: None, 121162: None, 121163: None, 121164: None, 121165: None, 121166: None, 121167: None, 121168: None, 121169: None, 121170: None, 121171: None, 121172: None, 121173: None, 121174: None, 121175: None, 121176: None, 121177: None, 121178: None, 121179: None, 121180: None, 121181: None, 121182: None, 121183: None, 121184: None, 121185: None, 121186: None, 121187: None, 121188: None, 121189: None, 121190: None, 121191: None, 121192: None, 121193: None, 121194: None, 121195: None, 121196: None, 121197: None, 121198: None, 121199: None, 121200: None, 121201: None, 121202: None, 121203: None, 121204: None, 121205: None, 121206: None, 121207: None, 121208: None, 121209: None, 121210: None, 121211: None, 121212: None, 121213: None, 121214: None, 121215: None, 121216: None, 121217: None, 121218: None, 121219: None, 121220: None, 121221: None, 121222: None, 121223: None, 121224: None, 121225: None, 121226: None, 121227: None, 121228: None, 121229: None, 121230: None, 121231: None, 121232: None, 121233: None, 121234: None, 121235: None, 121236: None, 121237: None, 121238: None, 121239: None, 121240: None, 121241: None, 121242: None, 121243: None, 121244: None, 121245: None, 121246: None, 121247: None, 121248: None, 121249: None, 121250: None, 121251: None, 121252: None, 121253: None, 121254: None, 121255: None, 121256: None, 121257: None, 121258: None, 121259: None, 121260: None, 121261: None, 121262: None, 121263: None, 121264: None, 121265: None, 121266: None, 121267: None, 121268: None, 121269: None, 121270: None, 121271: None, 121272: None, 121273: None, 121274: None, 121275: None, 121276: None, 121277: None, 121278: None, 121279: None, 121280: None, 121281: None, 121282: None, 121283: None, 121284: None, 121285: None, 121286: None, 121287: None, 121288: None, 121289: None, 121290: None, 121291: None, 121292: None, 121293: None, 121294: None, 121295: None, 121296: None, 121297: None, 121298: None, 121299: None, 121300: None, 121301: None, 121302: None, 121303: None, 121304: None, 121305: None, 121306: None, 121307: None, 121308: None, 121309: None, 121310: None, 121311: None, 121312: None, 121313: None, 121314: None, 121315: None, 121316: None, 121317: None, 121318: None, 121319: None, 121320: None, 121321: None, 121322: None, 121323: None, 121324: None, 121325: None, 121326: None, 121327: None, 121328: None, 121329: None, 121330: None, 121331: None, 121332: None, 121333: None, 121334: None, 121335: None, 121336: None, 121337: None, 121338: None, 121339: None, 121340: None, 121341: None, 121342: None, 121343: None, 121399: None, 121400: None, 121401: None, 121402: None, 121453: None, 121454: None, 121455: None, 121456: None, 121457: None, 121458: None, 121459: None, 121460: None, 121462: None, 121463: None, 121464: None, 121465: None, 121466: None, 121467: None, 121468: None, 121469: None, 121470: None, 121471: None, 121472: None, 121473: None, 121474: None, 121475: None, 121477: None, 121478: None, 121479: None, 121480: None, 121481: None, 121482: None, 121483: None, 125278: None, 125279: None, 126124: None, 126128: None, 126704: None, 126705: None, 126976: None, 126977: None, 126978: None, 126979: None, 126980: None, 126981: None, 126982: None, 126983: None, 126984: None, 126985: None, 126986: None, 126987: None, 126988: None, 126989: None, 126990: None, 126991: None, 126992: None, 126993: None, 126994: None, 126995: None, 126996: None, 126997: None, 126998: None, 126999: None, 127000: None, 127001: None, 127002: None, 127003: None, 127004: None, 127005: None, 127006: None, 127007: None, 127008: None, 127009: None, 127010: None, 127011: None, 127012: None, 127013: None, 127014: None, 127015: None, 127016: None, 127017: None, 127018: None, 127019: None, 127024: None, 127025: None, 127026: None, 127027: None, 127028: None, 127029: None, 127030: None, 127031: None, 127032: None, 127033: None, 127034: None, 127035: None, 127036: None, 127037: None, 127038: None, 127039: None, 127040: None, 127041: None, 127042: None, 127043: None, 127044: None, 127045: None, 127046: None, 127047: None, 127048: None, 127049: None, 127050: None, 127051: None, 127052: None, 127053: None, 127054: None, 127055: None, 127056: None, 127057: None, 127058: None, 127059: None, 127060: None, 127061: None, 127062: None, 127063: None, 127064: None, 127065: None, 127066: None, 127067: None, 127068: None, 127069: None, 127070: None, 127071: None, 127072: None, 127073: None, 127074: None, 127075: None, 127076: None, 127077: None, 127078: None, 127079: None, 127080: None, 127081: None, 127082: None, 127083: None, 127084: None, 127085: None, 127086: None, 127087: None, 127088: None, 127089: None, 127090: None, 127091: None, 127092: None, 127093: None, 127094: None, 127095: None, 127096: None, 127097: None, 127098: None, 127099: None, 127100: None, 127101: None, 127102: None, 127103: None, 127104: None, 127105: None, 127106: None, 127107: None, 127108: None, 127109: None, 127110: None, 127111: None, 127112: None, 127113: None, 127114: None, 127115: None, 127116: None, 127117: None, 127118: None, 127119: None, 127120: None, 127121: None, 127122: None, 127123: None, 127136: None, 127137: None, 127138: None, 127139: None, 127140: None, 127141: None, 127142: None, 127143: None, 127144: None, 127145: None, 127146: None, 127147: None, 127148: None, 127149: None, 127150: None, 127153: None, 127154: None, 127155: None, 127156: None, 127157: None, 127158: None, 127159: None, 127160: None, 127161: None, 127162: None, 127163: None, 127164: None, 127165: None, 127166: None, 127167: None, 127169: None, 127170: None, 127171: None, 127172: None, 127173: None, 127174: None, 127175: None, 127176: None, 127177: None, 127178: None, 127179: None, 127180: None, 127181: None, 127182: None, 127183: None, 127185: None, 127186: None, 127187: None, 127188: None, 127189: None, 127190: None, 127191: None, 127192: None, 127193: None, 127194: None, 127195: None, 127196: None, 127197: None, 127198: None, 127199: None, 127200: None, 127201: None, 127202: None, 127203: None, 127204: None, 127205: None, 127206: None, 127207: None, 127208: None, 127209: None, 127210: None, 127211: None, 127212: None, 127213: None, 127214: None, 127215: None, 127216: None, 127217: None, 127218: None, 127219: None, 127220: None, 127221: None, 127248: None, 127249: None, 127250: None, 127251: None, 127252: None, 127253: None, 127254: None, 127255: None, 127256: None, 127257: None, 127258: None, 127259: None, 127260: None, 127261: None, 127262: None, 127263: None, 127264: None, 127265: None, 127266: None, 127267: None, 127268: None, 127269: None, 127270: None, 127271: None, 127272: None, 127273: None, 127274: None, 127275: None, 127276: None, 127277: None, 127278: None, 127279: None, 127280: None, 127281: None, 127282: None, 127283: None, 127284: None, 127285: None, 127286: None, 127287: None, 127288: None, 127289: None, 127290: None, 127291: None, 127292: None, 127293: None, 127294: None, 127295: None, 127296: None, 127297: None, 127298: None, 127299: None, 127300: None, 127301: None, 127302: None, 127303: None, 127304: None, 127305: None, 127306: None, 127307: None, 127308: None, 127309: None, 127310: None, 127311: None, 127312: None, 127313: None, 127314: None, 127315: None, 127316: None, 127317: None, 127318: None, 127319: None, 127320: None, 127321: None, 127322: None, 127323: None, 127324: None, 127325: None, 127326: None, 127327: None, 127328: None, 127329: None, 127330: None, 127331: None, 127332: None, 127333: None, 127334: None, 127335: None, 127336: None, 127337: None, 127338: None, 127339: None, 127344: None, 127345: None, 127346: None, 127347: None, 127348: None, 127349: None, 127350: None, 127351: None, 127352: None, 127353: None, 127354: None, 127355: None, 127356: None, 127357: None, 127358: None, 127359: None, 127360: None, 127361: None, 127362: None, 127363: None, 127364: None, 127365: None, 127366: None, 127367: None, 127368: None, 127369: None, 127370: None, 127371: None, 127372: None, 127373: None, 127374: None, 127375: None, 127376: None, 127377: None, 127378: None, 127379: None, 127380: None, 127381: None, 127382: None, 127383: None, 127384: None, 127385: None, 127386: None, 127387: None, 127388: None, 127389: None, 127390: None, 127391: None, 127392: None, 127393: None, 127394: None, 127395: None, 127396: None, 127397: None, 127398: None, 127399: None, 127400: None, 127401: None, 127402: None, 127403: None, 127404: None, 127462: None, 127463: None, 127464: None, 127465: None, 127466: None, 127467: None, 127468: None, 127469: None, 127470: None, 127471: None, 127472: None, 127473: None, 127474: None, 127475: None, 127476: None, 127477: None, 127478: None, 127479: None, 127480: None, 127481: None, 127482: None, 127483: None, 127484: None, 127485: None, 127486: None, 127487: None, 127488: None, 127489: None, 127490: None, 127504: None, 127505: None, 127506: None, 127507: None, 127508: None, 127509: None, 127510: None, 127511: None, 127512: None, 127513: None, 127514: None, 127515: None, 127516: None, 127517: None, 127518: None, 127519: None, 127520: None, 127521: None, 127522: None, 127523: None, 127524: None, 127525: None, 127526: None, 127527: None, 127528: None, 127529: None, 127530: None, 127531: None, 127532: None, 127533: None, 127534: None, 127535: None, 127536: None, 127537: None, 127538: None, 127539: None, 127540: None, 127541: None, 127542: None, 127543: None, 127544: None, 127545: None, 127546: None, 127547: None, 127552: None, 127553: None, 127554: None, 127555: None, 127556: None, 127557: None, 127558: None, 127559: None, 127560: None, 127568: None, 127569: None, 127584: None, 127585: None, 127586: None, 127587: None, 127588: None, 127589: None, 127744: None, 127745: None, 127746: None, 127747: None, 127748: None, 127749: None, 127750: None, 127751: None, 127752: None, 127753: None, 127754: None, 127755: None, 127756: None, 127757: None, 127758: None, 127759: None, 127760: None, 127761: None, 127762: None, 127763: None, 127764: None, 127765: None, 127766: None, 127767: None, 127768: None, 127769: None, 127770: None, 127771: None, 127772: None, 127773: None, 127774: None, 127775: None, 127776: None, 127777: None, 127778: None, 127779: None, 127780: None, 127781: None, 127782: None, 127783: None, 127784: None, 127785: None, 127786: None, 127787: None, 127788: None, 127789: None, 127790: None, 127791: None, 127792: None, 127793: None, 127794: None, 127795: None, 127796: None, 127797: None, 127798: None, 127799: None, 127800: None, 127801: None, 127802: None, 127803: None, 127804: None, 127805: None, 127806: None, 127807: None, 127808: None, 127809: None, 127810: None, 127811: None, 127812: None, 127813: None, 127814: None, 127815: None, 127816: None, 127817: None, 127818: None, 127819: None, 127820: None, 127821: None, 127822: None, 127823: None, 127824: None, 127825: None, 127826: None, 127827: None, 127828: None, 127829: None, 127830: None, 127831: None, 127832: None, 127833: None, 127834: None, 127835: None, 127836: None, 127837: None, 127838: None, 127839: None, 127840: None, 127841: None, 127842: None, 127843: None, 127844: None, 127845: None, 127846: None, 127847: None, 127848: None, 127849: None, 127850: None, 127851: None, 127852: None, 127853: None, 127854: None, 127855: None, 127856: None, 127857: None, 127858: None, 127859: None, 127860: None, 127861: None, 127862: None, 127863: None, 127864: None, 127865: None, 127866: None, 127867: None, 127868: None, 127869: None, 127870: None, 127871: None, 127872: None, 127873: None, 127874: None, 127875: None, 127876: None, 127877: None, 127878: None, 127879: None, 127880: None, 127881: None, 127882: None, 127883: None, 127884: None, 127885: None, 127886: None, 127887: None, 127888: None, 127889: None, 127890: None, 127891: None, 127892: None, 127893: None, 127894: None, 127895: None, 127896: None, 127897: None, 127898: None, 127899: None, 127900: None, 127901: None, 127902: None, 127903: None, 127904: None, 127905: None, 127906: None, 127907: None, 127908: None, 127909: None, 127910: None, 127911: None, 127912: None, 127913: None, 127914: None, 127915: None, 127916: None, 127917: None, 127918: None, 127919: None, 127920: None, 127921: None, 127922: None, 127923: None, 127924: None, 127925: None, 127926: None, 127927: None, 127928: None, 127929: None, 127930: None, 127931: None, 127932: None, 127933: None, 127934: None, 127935: None, 127936: None, 127937: None, 127938: None, 127939: None, 127940: None, 127941: None, 127942: None, 127943: None, 127944: None, 127945: None, 127946: None, 127947: None, 127948: None, 127949: None, 127950: None, 127951: None, 127952: None, 127953: None, 127954: None, 127955: None, 127956: None, 127957: None, 127958: None, 127959: None, 127960: None, 127961: None, 127962: None, 127963: None, 127964: None, 127965: None, 127966: None, 127967: None, 127968: None, 127969: None, 127970: None, 127971: None, 127972: None, 127973: None, 127974: None, 127975: None, 127976: None, 127977: None, 127978: None, 127979: None, 127980: None, 127981: None, 127982: None, 127983: None, 127984: None, 127985: None, 127986: None, 127987: None, 127988: None, 127989: None, 127990: None, 127991: None, 127992: None, 127993: None, 127994: None, 127995: None, 127996: None, 127997: None, 127998: None, 127999: None, 128000: None, 128001: None, 128002: None, 128003: None, 128004: None, 128005: None, 128006: None, 128007: None, 128008: None, 128009: None, 128010: None, 128011: None, 128012: None, 128013: None, 128014: None, 128015: None, 128016: None, 128017: None, 128018: None, 128019: None, 128020: None, 128021: None, 128022: None, 128023: None, 128024: None, 128025: None, 128026: None, 128027: None, 128028: None, 128029: None, 128030: None, 128031: None, 128032: None, 128033: None, 128034: None, 128035: None, 128036: None, 128037: None, 128038: None, 128039: None, 128040: None, 128041: None, 128042: None, 128043: None, 128044: None, 128045: None, 128046: None, 128047: None, 128048: None, 128049: None, 128050: None, 128051: None, 128052: None, 128053: None, 128054: None, 128055: None, 128056: None, 128057: None, 128058: None, 128059: None, 128060: None, 128061: None, 128062: None, 128063: None, 128064: None, 128065: None, 128066: None, 128067: None, 128068: None, 128069: None, 128070: None, 128071: None, 128072: None, 128073: None, 128074: None, 128075: None, 128076: None, 128077: None, 128078: None, 128079: None, 128080: None, 128081: None, 128082: None, 128083: None, 128084: None, 128085: None, 128086: None, 128087: None, 128088: None, 128089: None, 128090: None, 128091: None, 128092: None, 128093: None, 128094: None, 128095: None, 128096: None, 128097: None, 128098: None, 128099: None, 128100: None, 128101: None, 128102: None, 128103: None, 128104: None, 128105: None, 128106: None, 128107: None, 128108: None, 128109: None, 128110: None, 128111: None, 128112: None, 128113: None, 128114: None, 128115: None, 128116: None, 128117: None, 128118: None, 128119: None, 128120: None, 128121: None, 128122: None, 128123: None, 128124: None, 128125: None, 128126: None, 128127: None, 128128: None, 128129: None, 128130: None, 128131: None, 128132: None, 128133: None, 128134: None, 128135: None, 128136: None, 128137: None, 128138: None, 128139: None, 128140: None, 128141: None, 128142: None, 128143: None, 128144: None, 128145: None, 128146: None, 128147: None, 128148: None, 128149: None, 128150: None, 128151: None, 128152: None, 128153: None, 128154: None, 128155: None, 128156: None, 128157: None, 128158: None, 128159: None, 128160: None, 128161: None, 128162: None, 128163: None, 128164: None, 128165: None, 128166: None, 128167: None, 128168: None, 128169: None, 128170: None, 128171: None, 128172: None, 128173: None, 128174: None, 128175: None, 128176: None, 128177: None, 128178: None, 128179: None, 128180: None, 128181: None, 128182: None, 128183: None, 128184: None, 128185: None, 128186: None, 128187: None, 128188: None, 128189: None, 128190: None, 128191: None, 128192: None, 128193: None, 128194: None, 128195: None, 128196: None, 128197: None, 128198: None, 128199: None, 128200: None, 128201: None, 128202: None, 128203: None, 128204: None, 128205: None, 128206: None, 128207: None, 128208: None, 128209: None, 128210: None, 128211: None, 128212: None, 128213: None, 128214: None, 128215: None, 128216: None, 128217: None, 128218: None, 128219: None, 128220: None, 128221: None, 128222: None, 128223: None, 128224: None, 128225: None, 128226: None, 128227: None, 128228: None, 128229: None, 128230: None, 128231: None, 128232: None, 128233: None, 128234: None, 128235: None, 128236: None, 128237: None, 128238: None, 128239: None, 128240: None, 128241: None, 128242: None, 128243: None, 128244: None, 128245: None, 128246: None, 128247: None, 128248: None, 128249: None, 128250: None, 128251: None, 128252: None, 128253: None, 128254: None, 128255: None, 128256: None, 128257: None, 128258: None, 128259: None, 128260: None, 128261: None, 128262: None, 128263: None, 128264: None, 128265: None, 128266: None, 128267: None, 128268: None, 128269: None, 128270: None, 128271: None, 128272: None, 128273: None, 128274: None, 128275: None, 128276: None, 128277: None, 128278: None, 128279: None, 128280: None, 128281: None, 128282: None, 128283: None, 128284: None, 128285: None, 128286: None, 128287: None, 128288: None, 128289: None, 128290: None, 128291: None, 128292: None, 128293: None, 128294: None, 128295: None, 128296: None, 128297: None, 128298: None, 128299: None, 128300: None, 128301: None, 128302: None, 128303: None, 128304: None, 128305: None, 128306: None, 128307: None, 128308: None, 128309: None, 128310: None, 128311: None, 128312: None, 128313: None, 128314: None, 128315: None, 128316: None, 128317: None, 128318: None, 128319: None, 128320: None, 128321: None, 128322: None, 128323: None, 128324: None, 128325: None, 128326: None, 128327: None, 128328: None, 128329: None, 128330: None, 128331: None, 128332: None, 128333: None, 128334: None, 128335: None, 128336: None, 128337: None, 128338: None, 128339: None, 128340: None, 128341: None, 128342: None, 128343: None, 128344: None, 128345: None, 128346: None, 128347: None, 128348: None, 128349: None, 128350: None, 128351: None, 128352: None, 128353: None, 128354: None, 128355: None, 128356: None, 128357: None, 128358: None, 128359: None, 128360: None, 128361: None, 128362: None, 128363: None, 128364: None, 128365: None, 128366: None, 128367: None, 128368: None, 128369: None, 128370: None, 128371: None, 128372: None, 128373: None, 128374: None, 128375: None, 128376: None, 128377: None, 128378: None, 128379: None, 128380: None, 128381: None, 128382: None, 128383: None, 128384: None, 128385: None, 128386: None, 128387: None, 128388: None, 128389: None, 128390: None, 128391: None, 128392: None, 128393: None, 128394: None, 128395: None, 128396: None, 128397: None, 128398: None, 128399: None, 128400: None, 128401: None, 128402: None, 128403: None, 128404: None, 128405: None, 128406: None, 128407: None, 128408: None, 128409: None, 128410: None, 128411: None, 128412: None, 128413: None, 128414: None, 128415: None, 128416: None, 128417: None, 128418: None, 128419: None, 128420: None, 128421: None, 128422: None, 128423: None, 128424: None, 128425: None, 128426: None, 128427: None, 128428: None, 128429: None, 128430: None, 128431: None, 128432: None, 128433: None, 128434: None, 128435: None, 128436: None, 128437: None, 128438: None, 128439: None, 128440: None, 128441: None, 128442: None, 128443: None, 128444: None, 128445: None, 128446: None, 128447: None, 128448: None, 128449: None, 128450: None, 128451: None, 128452: None, 128453: None, 128454: None, 128455: None, 128456: None, 128457: None, 128458: None, 128459: None, 128460: None, 128461: None, 128462: None, 128463: None, 128464: None, 128465: None, 128466: None, 128467: None, 128468: None, 128469: None, 128470: None, 128471: None, 128472: None, 128473: None, 128474: None, 128475: None, 128476: None, 128477: None, 128478: None, 128479: None, 128480: None, 128481: None, 128482: None, 128483: None, 128484: None, 128485: None, 128486: None, 128487: None, 128488: None, 128489: None, 128490: None, 128491: None, 128492: None, 128493: None, 128494: None, 128495: None, 128496: None, 128497: None, 128498: None, 128499: None, 128500: None, 128501: None, 128502: None, 128503: None, 128504: None, 128505: None, 128506: None, 128507: None, 128508: None, 128509: None, 128510: None, 128511: None, 128512: None, 128513: None, 128514: None, 128515: None, 128516: None, 128517: None, 128518: None, 128519: None, 128520: None, 128521: None, 128522: None, 128523: None, 128524: None, 128525: None, 128526: None, 128527: None, 128528: None, 128529: None, 128530: None, 128531: None, 128532: None, 128533: None, 128534: None, 128535: None, 128536: None, 128537: None, 128538: None, 128539: None, 128540: None, 128541: None, 128542: None, 128543: None, 128544: None, 128545: None, 128546: None, 128547: None, 128548: None, 128549: None, 128550: None, 128551: None, 128552: None, 128553: None, 128554: None, 128555: None, 128556: None, 128557: None, 128558: None, 128559: None, 128560: None, 128561: None, 128562: None, 128563: None, 128564: None, 128565: None, 128566: None, 128567: None, 128568: None, 128569: None, 128570: None, 128571: None, 128572: None, 128573: None, 128574: None, 128575: None, 128576: None, 128577: None, 128578: None, 128579: None, 128580: None, 128581: None, 128582: None, 128583: None, 128584: None, 128585: None, 128586: None, 128587: None, 128588: None, 128589: None, 128590: None, 128591: None, 128592: None, 128593: None, 128594: None, 128595: None, 128596: None, 128597: None, 128598: None, 128599: None, 128600: None, 128601: None, 128602: None, 128603: None, 128604: None, 128605: None, 128606: None, 128607: None, 128608: None, 128609: None, 128610: None, 128611: None, 128612: None, 128613: None, 128614: None, 128615: None, 128616: None, 128617: None, 128618: None, 128619: None, 128620: None, 128621: None, 128622: None, 128623: None, 128624: None, 128625: None, 128626: None, 128627: None, 128628: None, 128629: None, 128630: None, 128631: None, 128632: None, 128633: None, 128634: None, 128635: None, 128636: None, 128637: None, 128638: None, 128639: None, 128640: None, 128641: None, 128642: None, 128643: None, 128644: None, 128645: None, 128646: None, 128647: None, 128648: None, 128649: None, 128650: None, 128651: None, 128652: None, 128653: None, 128654: None, 128655: None, 128656: None, 128657: None, 128658: None, 128659: None, 128660: None, 128661: None, 128662: None, 128663: None, 128664: None, 128665: None, 128666: None, 128667: None, 128668: None, 128669: None, 128670: None, 128671: None, 128672: None, 128673: None, 128674: None, 128675: None, 128676: None, 128677: None, 128678: None, 128679: None, 128680: None, 128681: None, 128682: None, 128683: None, 128684: None, 128685: None, 128686: None, 128687: None, 128688: None, 128689: None, 128690: None, 128691: None, 128692: None, 128693: None, 128694: None, 128695: None, 128696: None, 128697: None, 128698: None, 128699: None, 128700: None, 128701: None, 128702: None, 128703: None, 128704: None, 128705: None, 128706: None, 128707: None, 128708: None, 128709: None, 128710: None, 128711: None, 128712: None, 128713: None, 128714: None, 128715: None, 128716: None, 128717: None, 128718: None, 128719: None, 128720: None, 128721: None, 128722: None, 128723: None, 128724: None, 128736: None, 128737: None, 128738: None, 128739: None, 128740: None, 128741: None, 128742: None, 128743: None, 128744: None, 128745: None, 128746: None, 128747: None, 128748: None, 128752: None, 128753: None, 128754: None, 128755: None, 128756: None, 128757: None, 128758: None, 128759: None, 128760: None, 128761: None, 128768: None, 128769: None, 128770: None, 128771: None, 128772: None, 128773: None, 128774: None, 128775: None, 128776: None, 128777: None, 128778: None, 128779: None, 128780: None, 128781: None, 128782: None, 128783: None, 128784: None, 128785: None, 128786: None, 128787: None, 128788: None, 128789: None, 128790: None, 128791: None, 128792: None, 128793: None, 128794: None, 128795: None, 128796: None, 128797: None, 128798: None, 128799: None, 128800: None, 128801: None, 128802: None, 128803: None, 128804: None, 128805: None, 128806: None, 128807: None, 128808: None, 128809: None, 128810: None, 128811: None, 128812: None, 128813: None, 128814: None, 128815: None, 128816: None, 128817: None, 128818: None, 128819: None, 128820: None, 128821: None, 128822: None, 128823: None, 128824: None, 128825: None, 128826: None, 128827: None, 128828: None, 128829: None, 128830: None, 128831: None, 128832: None, 128833: None, 128834: None, 128835: None, 128836: None, 128837: None, 128838: None, 128839: None, 128840: None, 128841: None, 128842: None, 128843: None, 128844: None, 128845: None, 128846: None, 128847: None, 128848: None, 128849: None, 128850: None, 128851: None, 128852: None, 128853: None, 128854: None, 128855: None, 128856: None, 128857: None, 128858: None, 128859: None, 128860: None, 128861: None, 128862: None, 128863: None, 128864: None, 128865: None, 128866: None, 128867: None, 128868: None, 128869: None, 128870: None, 128871: None, 128872: None, 128873: None, 128874: None, 128875: None, 128876: None, 128877: None, 128878: None, 128879: None, 128880: None, 128881: None, 128882: None, 128883: None, 128896: None, 128897: None, 128898: None, 128899: None, 128900: None, 128901: None, 128902: None, 128903: None, 128904: None, 128905: None, 128906: None, 128907: None, 128908: None, 128909: None, 128910: None, 128911: None, 128912: None, 128913: None, 128914: None, 128915: None, 128916: None, 128917: None, 128918: None, 128919: None, 128920: None, 128921: None, 128922: None, 128923: None, 128924: None, 128925: None, 128926: None, 128927: None, 128928: None, 128929: None, 128930: None, 128931: None, 128932: None, 128933: None, 128934: None, 128935: None, 128936: None, 128937: None, 128938: None, 128939: None, 128940: None, 128941: None, 128942: None, 128943: None, 128944: None, 128945: None, 128946: None, 128947: None, 128948: None, 128949: None, 128950: None, 128951: None, 128952: None, 128953: None, 128954: None, 128955: None, 128956: None, 128957: None, 128958: None, 128959: None, 128960: None, 128961: None, 128962: None, 128963: None, 128964: None, 128965: None, 128966: None, 128967: None, 128968: None, 128969: None, 128970: None, 128971: None, 128972: None, 128973: None, 128974: None, 128975: None, 128976: None, 128977: None, 128978: None, 128979: None, 128980: None, 128981: None, 128982: None, 128983: None, 128984: None, 129024: None, 129025: None, 129026: None, 129027: None, 129028: None, 129029: None, 129030: None, 129031: None, 129032: None, 129033: None, 129034: None, 129035: None, 129040: None, 129041: None, 129042: None, 129043: None, 129044: None, 129045: None, 129046: None, 129047: None, 129048: None, 129049: None, 129050: None, 129051: None, 129052: None, 129053: None, 129054: None, 129055: None, 129056: None, 129057: None, 129058: None, 129059: None, 129060: None, 129061: None, 129062: None, 129063: None, 129064: None, 129065: None, 129066: None, 129067: None, 129068: None, 129069: None, 129070: None, 129071: None, 129072: None, 129073: None, 129074: None, 129075: None, 129076: None, 129077: None, 129078: None, 129079: None, 129080: None, 129081: None, 129082: None, 129083: None, 129084: None, 129085: None, 129086: None, 129087: None, 129088: None, 129089: None, 129090: None, 129091: None, 129092: None, 129093: None, 129094: None, 129095: None, 129104: None, 129105: None, 129106: None, 129107: None, 129108: None, 129109: None, 129110: None, 129111: None, 129112: None, 129113: None, 129120: None, 129121: None, 129122: None, 129123: None, 129124: None, 129125: None, 129126: None, 129127: None, 129128: None, 129129: None, 129130: None, 129131: None, 129132: None, 129133: None, 129134: None, 129135: None, 129136: None, 129137: None, 129138: None, 129139: None, 129140: None, 129141: None, 129142: None, 129143: None, 129144: None, 129145: None, 129146: None, 129147: None, 129148: None, 129149: None, 129150: None, 129151: None, 129152: None, 129153: None, 129154: None, 129155: None, 129156: None, 129157: None, 129158: None, 129159: None, 129168: None, 129169: None, 129170: None, 129171: None, 129172: None, 129173: None, 129174: None, 129175: None, 129176: None, 129177: None, 129178: None, 129179: None, 129180: None, 129181: None, 129182: None, 129183: None, 129184: None, 129185: None, 129186: None, 129187: None, 129188: None, 129189: None, 129190: None, 129191: None, 129192: None, 129193: None, 129194: None, 129195: None, 129196: None, 129197: None, 129280: None, 129281: None, 129282: None, 129283: None, 129284: None, 129285: None, 129286: None, 129287: None, 129288: None, 129289: None, 129290: None, 129291: None, 129296: None, 129297: None, 129298: None, 129299: None, 129300: None, 129301: None, 129302: None, 129303: None, 129304: None, 129305: None, 129306: None, 129307: None, 129308: None, 129309: None, 129310: None, 129311: None, 129312: None, 129313: None, 129314: None, 129315: None, 129316: None, 129317: None, 129318: None, 129319: None, 129320: None, 129321: None, 129322: None, 129323: None, 129324: None, 129325: None, 129326: None, 129327: None, 129328: None, 129329: None, 129330: None, 129331: None, 129332: None, 129333: None, 129334: None, 129335: None, 129336: None, 129337: None, 129338: None, 129339: None, 129340: None, 129341: None, 129342: None, 129344: None, 129345: None, 129346: None, 129347: None, 129348: None, 129349: None, 129350: None, 129351: None, 129352: None, 129353: None, 129354: None, 129355: None, 129356: None, 129357: None, 129358: None, 129359: None, 129360: None, 129361: None, 129362: None, 129363: None, 129364: None, 129365: None, 129366: None, 129367: None, 129368: None, 129369: None, 129370: None, 129371: None, 129372: None, 129373: None, 129374: None, 129375: None, 129376: None, 129377: None, 129378: None, 129379: None, 129380: None, 129381: None, 129382: None, 129383: None, 129384: None, 129385: None, 129386: None, 129387: None, 129388: None, 129389: None, 129390: None, 129391: None, 129392: None, 129395: None, 129396: None, 129397: None, 129398: None, 129402: None, 129404: None, 129405: None, 129406: None, 129407: None, 129408: None, 129409: None, 129410: None, 129411: None, 129412: None, 129413: None, 129414: None, 129415: None, 129416: None, 129417: None, 129418: None, 129419: None, 129420: None, 129421: None, 129422: None, 129423: None, 129424: None, 129425: None, 129426: None, 129427: None, 129428: None, 129429: None, 129430: None, 129431: None, 129432: None, 129433: None, 129434: None, 129435: None, 129436: None, 129437: None, 129438: None, 129439: None, 129440: None, 129441: None, 129442: None, 129456: None, 129457: None, 129458: None, 129459: None, 129460: None, 129461: None, 129462: None, 129463: None, 129464: None, 129465: None, 129472: None, 129473: None, 129474: None, 129488: None, 129489: None, 129490: None, 129491: None, 129492: None, 129493: None, 129494: None, 129495: None, 129496: None, 129497: None, 129498: None, 129499: None, 129500: None, 129501: None, 129502: None, 129503: None, 129504: None, 129505: None, 129506: None, 129507: None, 129508: None, 129509: None, 129510: None, 129511: None, 129512: None, 129513: None, 129514: None, 129515: None, 129516: None, 129517: None, 129518: None, 129519: None, 129520: None, 129521: None, 129522: None, 129523: None, 129524: None, 129525: None, 129526: None, 129527: None, 129528: None, 129529: None, 129530: None, 129531: None, 129532: None, 129533: None, 129534: None, 129535: None, 129632: None, 129633: None, 129634: None, 129635: None, 129636: None, 129637: None, 129638: None, 129639: None, 129640: None, 129641: None, 129642: None, 129643: None, 129644: None, 129645: None}

ORD_DIGIT_TO_NONE = {48: None, 49: None, 50: None, 51: None, 52: None, 53: None, 54: None, 55: None, 56: None, 57: None, 178: None, 179: None, 185: None, 188: None, 189: None, 190: None, 1632: None, 1633: None, 1634: None, 1635: None, 1636: None, 1637: None, 1638: None, 1639: None, 1640: None, 1641: None, 1776: None, 1777: None, 1778: None, 1779: None, 1780: None, 1781: None, 1782: None, 1783: None, 1784: None, 1785: None, 1984: None, 1985: None, 1986: None, 1987: None, 1988: None, 1989: None, 1990: None, 1991: None, 1992: None, 1993: None, 2406: None, 2407: None, 2408: None, 2409: None, 2410: None, 2411: None, 2412: None, 2413: None, 2414: None, 2415: None, 2534: None, 2535: None, 2536: None, 2537: None, 2538: None, 2539: None, 2540: None, 2541: None, 2542: None, 2543: None, 2548: None, 2549: None, 2550: None, 2551: None, 2552: None, 2553: None, 2662: None, 2663: None, 2664: None, 2665: None, 2666: None, 2667: None, 2668: None, 2669: None, 2670: None, 2671: None, 2790: None, 2791: None, 2792: None, 2793: None, 2794: None, 2795: None, 2796: None, 2797: None, 2798: None, 2799: None, 2918: None, 2919: None, 2920: None, 2921: None, 2922: None, 2923: None, 2924: None, 2925: None, 2926: None, 2927: None, 2930: None, 2931: None, 2932: None, 2933: None, 2934: None, 2935: None, 3046: None, 3047: None, 3048: None, 3049: None, 3050: None, 3051: None, 3052: None, 3053: None, 3054: None, 3055: None, 3056: None, 3057: None, 3058: None, 3174: None, 3175: None, 3176: None, 3177: None, 3178: None, 3179: None, 3180: None, 3181: None, 3182: None, 3183: None, 3192: None, 3193: None, 3194: None, 3195: None, 3196: None, 3197: None, 3198: None, 3302: None, 3303: None, 3304: None, 3305: None, 3306: None, 3307: None, 3308: None, 3309: None, 3310: None, 3311: None, 3416: None, 3417: None, 3418: None, 3419: None, 3420: None, 3421: None, 3422: None, 3430: None, 3431: None, 3432: None, 3433: None, 3434: None, 3435: None, 3436: None, 3437: None, 3438: None, 3439: None, 3440: None, 3441: None, 3442: None, 3443: None, 3444: None, 3445: None, 3446: None, 3447: None, 3448: None, 3558: None, 3559: None, 3560: None, 3561: None, 3562: None, 3563: None, 3564: None, 3565: None, 3566: None, 3567: None, 3664: None, 3665: None, 3666: None, 3667: None, 3668: None, 3669: None, 3670: None, 3671: None, 3672: None, 3673: None, 3792: None, 3793: None, 3794: None, 3795: None, 3796: None, 3797: None, 3798: None, 3799: None, 3800: None, 3801: None, 3872: None, 3873: None, 3874: None, 3875: None, 3876: None, 3877: None, 3878: None, 3879: None, 3880: None, 3881: None, 3882: None, 3883: None, 3884: None, 3885: None, 3886: None, 3887: None, 3888: None, 3889: None, 3890: None, 3891: None, 4160: None, 4161: None, 4162: None, 4163: None, 4164: None, 4165: None, 4166: None, 4167: None, 4168: None, 4169: None, 4240: None, 4241: None, 4242: None, 4243: None, 4244: None, 4245: None, 4246: None, 4247: None, 4248: None, 4249: None, 4969: None, 4970: None, 4971: None, 4972: None, 4973: None, 4974: None, 4975: None, 4976: None, 4977: None, 4978: None, 4979: None, 4980: None, 4981: None, 4982: None, 4983: None, 4984: None, 4985: None, 4986: None, 4987: None, 4988: None, 5870: None, 5871: None, 5872: None, 6112: None, 6113: None, 6114: None, 6115: None, 6116: None, 6117: None, 6118: None, 6119: None, 6120: None, 6121: None, 6128: None, 6129: None, 6130: None, 6131: None, 6132: None, 6133: None, 6134: None, 6135: None, 6136: None, 6137: None, 6160: None, 6161: None, 6162: None, 6163: None, 6164: None, 6165: None, 6166: None, 6167: None, 6168: None, 6169: None, 6470: None, 6471: None, 6472: None, 6473: None, 6474: None, 6475: None, 6476: None, 6477: None, 6478: None, 6479: None, 6608: None, 6609: None, 6610: None, 6611: None, 6612: None, 6613: None, 6614: None, 6615: None, 6616: None, 6617: None, 6618: None, 6784: None, 6785: None, 6786: None, 6787: None, 6788: None, 6789: None, 6790: None, 6791: None, 6792: None, 6793: None, 6800: None, 6801: None, 6802: None, 6803: None, 6804: None, 6805: None, 6806: None, 6807: None, 6808: None, 6809: None, 6992: None, 6993: None, 6994: None, 6995: None, 6996: None, 6997: None, 6998: None, 6999: None, 7000: None, 7001: None, 7088: None, 7089: None, 7090: None, 7091: None, 7092: None, 7093: None, 7094: None, 7095: None, 7096: None, 7097: None, 7232: None, 7233: None, 7234: None, 7235: None, 7236: None, 7237: None, 7238: None, 7239: None, 7240: None, 7241: None, 7248: None, 7249: None, 7250: None, 7251: None, 7252: None, 7253: None, 7254: None, 7255: None, 7256: None, 7257: None, 8304: None, 8308: None, 8309: None, 8310: None, 8311: None, 8312: None, 8313: None, 8320: None, 8321: None, 8322: None, 8323: None, 8324: None, 8325: None, 8326: None, 8327: None, 8328: None, 8329: None, 8528: None, 8529: None, 8530: None, 8531: None, 8532: None, 8533: None, 8534: None, 8535: None, 8536: None, 8537: None, 8538: None, 8539: None, 8540: None, 8541: None, 8542: None, 8543: None, 8544: None, 8545: None, 8546: None, 8547: None, 8548: None, 8549: None, 8550: None, 8551: None, 8552: None, 8553: None, 8554: None, 8555: None, 8556: None, 8557: None, 8558: None, 8559: None, 8560: None, 8561: None, 8562: None, 8563: None, 8564: None, 8565: None, 8566: None, 8567: None, 8568: None, 8569: None, 8570: None, 8571: None, 8572: None, 8573: None, 8574: None, 8575: None, 8576: None, 8577: None, 8578: None, 8581: None, 8582: None, 8583: None, 8584: None, 8585: None, 9312: None, 9313: None, 9314: None, 9315: None, 9316: None, 9317: None, 9318: None, 9319: None, 9320: None, 9321: None, 9322: None, 9323: None, 9324: None, 9325: None, 9326: None, 9327: None, 9328: None, 9329: None, 9330: None, 9331: None, 9332: None, 9333: None, 9334: None, 9335: None, 9336: None, 9337: None, 9338: None, 9339: None, 9340: None, 9341: None, 9342: None, 9343: None, 9344: None, 9345: None, 9346: None, 9347: None, 9348: None, 9349: None, 9350: None, 9351: None, 9352: None, 9353: None, 9354: None, 9355: None, 9356: None, 9357: None, 9358: None, 9359: None, 9360: None, 9361: None, 9362: None, 9363: None, 9364: None, 9365: None, 9366: None, 9367: None, 9368: None, 9369: None, 9370: None, 9371: None, 9450: None, 9451: None, 9452: None, 9453: None, 9454: None, 9455: None, 9456: None, 9457: None, 9458: None, 9459: None, 9460: None, 9461: None, 9462: None, 9463: None, 9464: None, 9465: None, 9466: None, 9467: None, 9468: None, 9469: None, 9470: None, 9471: None, 10102: None, 10103: None, 10104: None, 10105: None, 10106: None, 10107: None, 10108: None, 10109: None, 10110: None, 10111: None, 10112: None, 10113: None, 10114: None, 10115: None, 10116: None, 10117: None, 10118: None, 10119: None, 10120: None, 10121: None, 10122: None, 10123: None, 10124: None, 10125: None, 10126: None, 10127: None, 10128: None, 10129: None, 10130: None, 10131: None, 11517: None, 12295: None, 12321: None, 12322: None, 12323: None, 12324: None, 12325: None, 12326: None, 12327: None, 12328: None, 12329: None, 12344: None, 12345: None, 12346: None, 12690: None, 12691: None, 12692: None, 12693: None, 12832: None, 12833: None, 12834: None, 12835: None, 12836: None, 12837: None, 12838: None, 12839: None, 12840: None, 12841: None, 12872: None, 12873: None, 12874: None, 12875: None, 12876: None, 12877: None, 12878: None, 12879: None, 12881: None, 12882: None, 12883: None, 12884: None, 12885: None, 12886: None, 12887: None, 12888: None, 12889: None, 12890: None, 12891: None, 12892: None, 12893: None, 12894: None, 12895: None, 12928: None, 12929: None, 12930: None, 12931: None, 12932: None, 12933: None, 12934: None, 12935: None, 12936: None, 12937: None, 12977: None, 12978: None, 12979: None, 12980: None, 12981: None, 12982: None, 12983: None, 12984: None, 12985: None, 12986: None, 12987: None, 12988: None, 12989: None, 12990: None, 12991: None, 42528: None, 42529: None, 42530: None, 42531: None, 42532: None, 42533: None, 42534: None, 42535: None, 42536: None, 42537: None, 42726: None, 42727: None, 42728: None, 42729: None, 42730: None, 42731: None, 42732: None, 42733: None, 42734: None, 42735: None, 43056: None, 43057: None, 43058: None, 43059: None, 43060: None, 43061: None, 43216: None, 43217: None, 43218: None, 43219: None, 43220: None, 43221: None, 43222: None, 43223: None, 43224: None, 43225: None, 43264: None, 43265: None, 43266: None, 43267: None, 43268: None, 43269: None, 43270: None, 43271: None, 43272: None, 43273: None, 43472: None, 43473: None, 43474: None, 43475: None, 43476: None, 43477: None, 43478: None, 43479: None, 43480: None, 43481: None, 43504: None, 43505: None, 43506: None, 43507: None, 43508: None, 43509: None, 43510: None, 43511: None, 43512: None, 43513: None, 43600: None, 43601: None, 43602: None, 43603: None, 43604: None, 43605: None, 43606: None, 43607: None, 43608: None, 43609: None, 44016: None, 44017: None, 44018: None, 44019: None, 44020: None, 44021: None, 44022: None, 44023: None, 44024: None, 44025: None, 65296: None, 65297: None, 65298: None, 65299: None, 65300: None, 65301: None, 65302: None, 65303: None, 65304: None, 65305: None, 65799: None, 65800: None, 65801: None, 65802: None, 65803: None, 65804: None, 65805: None, 65806: None, 65807: None, 65808: None, 65809: None, 65810: None, 65811: None, 65812: None, 65813: None, 65814: None, 65815: None, 65816: None, 65817: None, 65818: None, 65819: None, 65820: None, 65821: None, 65822: None, 65823: None, 65824: None, 65825: None, 65826: None, 65827: None, 65828: None, 65829: None, 65830: None, 65831: None, 65832: None, 65833: None, 65834: None, 65835: None, 65836: None, 65837: None, 65838: None, 65839: None, 65840: None, 65841: None, 65842: None, 65843: None, 65856: None, 65857: None, 65858: None, 65859: None, 65860: None, 65861: None, 65862: None, 65863: None, 65864: None, 65865: None, 65866: None, 65867: None, 65868: None, 65869: None, 65870: None, 65871: None, 65872: None, 65873: None, 65874: None, 65875: None, 65876: None, 65877: None, 65878: None, 65879: None, 65880: None, 65881: None, 65882: None, 65883: None, 65884: None, 65885: None, 65886: None, 65887: None, 65888: None, 65889: None, 65890: None, 65891: None, 65892: None, 65893: None, 65894: None, 65895: None, 65896: None, 65897: None, 65898: None, 65899: None, 65900: None, 65901: None, 65902: None, 65903: None, 65904: None, 65905: None, 65906: None, 65907: None, 65908: None, 65909: None, 65910: None, 65911: None, 65912: None, 65930: None, 65931: None, 66273: None, 66274: None, 66275: None, 66276: None, 66277: None, 66278: None, 66279: None, 66280: None, 66281: None, 66282: None, 66283: None, 66284: None, 66285: None, 66286: None, 66287: None, 66288: None, 66289: None, 66290: None, 66291: None, 66292: None, 66293: None, 66294: None, 66295: None, 66296: None, 66297: None, 66298: None, 66299: None, 66336: None, 66337: None, 66338: None, 66339: None, 66369: None, 66378: None, 66513: None, 66514: None, 66515: None, 66516: None, 66517: None, 66720: None, 66721: None, 66722: None, 66723: None, 66724: None, 66725: None, 66726: None, 66727: None, 66728: None, 66729: None, 67672: None, 67673: None, 67674: None, 67675: None, 67676: None, 67677: None, 67678: None, 67679: None, 67705: None, 67706: None, 67707: None, 67708: None, 67709: None, 67710: None, 67711: None, 67751: None, 67752: None, 67753: None, 67754: None, 67755: None, 67756: None, 67757: None, 67758: None, 67759: None, 67835: None, 67836: None, 67837: None, 67838: None, 67839: None, 67862: None, 67863: None, 67864: None, 67865: None, 67866: None, 67867: None, 68028: None, 68029: None, 68032: None, 68033: None, 68034: None, 68035: None, 68036: None, 68037: None, 68038: None, 68039: None, 68040: None, 68041: None, 68042: None, 68043: None, 68044: None, 68045: None, 68046: None, 68047: None, 68050: None, 68051: None, 68052: None, 68053: None, 68054: None, 68055: None, 68056: None, 68057: None, 68058: None, 68059: None, 68060: None, 68061: None, 68062: None, 68063: None, 68064: None, 68065: None, 68066: None, 68067: None, 68068: None, 68069: None, 68070: None, 68071: None, 68072: None, 68073: None, 68074: None, 68075: None, 68076: None, 68077: None, 68078: None, 68079: None, 68080: None, 68081: None, 68082: None, 68083: None, 68084: None, 68085: None, 68086: None, 68087: None, 68088: None, 68089: None, 68090: None, 68091: None, 68092: None, 68093: None, 68094: None, 68095: None, 68160: None, 68161: None, 68162: None, 68163: None, 68164: None, 68165: None, 68166: None, 68167: None, 68168: None, 68221: None, 68222: None, 68253: None, 68254: None, 68255: None, 68331: None, 68332: None, 68333: None, 68334: None, 68335: None, 68440: None, 68441: None, 68442: None, 68443: None, 68444: None, 68445: None, 68446: None, 68447: None, 68472: None, 68473: None, 68474: None, 68475: None, 68476: None, 68477: None, 68478: None, 68479: None, 68521: None, 68522: None, 68523: None, 68524: None, 68525: None, 68526: None, 68527: None, 68858: None, 68859: None, 68860: None, 68861: None, 68862: None, 68863: None, 68912: None, 68913: None, 68914: None, 68915: None, 68916: None, 68917: None, 68918: None, 68919: None, 68920: None, 68921: None, 69216: None, 69217: None, 69218: None, 69219: None, 69220: None, 69221: None, 69222: None, 69223: None, 69224: None, 69225: None, 69226: None, 69227: None, 69228: None, 69229: None, 69230: None, 69231: None, 69232: None, 69233: None, 69234: None, 69235: None, 69236: None, 69237: None, 69238: None, 69239: None, 69240: None, 69241: None, 69242: None, 69243: None, 69244: None, 69245: None, 69246: None, 69405: None, 69406: None, 69407: None, 69408: None, 69409: None, 69410: None, 69411: None, 69412: None, 69413: None, 69414: None, 69457: None, 69458: None, 69459: None, 69460: None, 69714: None, 69715: None, 69716: None, 69717: None, 69718: None, 69719: None, 69720: None, 69721: None, 69722: None, 69723: None, 69724: None, 69725: None, 69726: None, 69727: None, 69728: None, 69729: None, 69730: None, 69731: None, 69732: None, 69733: None, 69734: None, 69735: None, 69736: None, 69737: None, 69738: None, 69739: None, 69740: None, 69741: None, 69742: None, 69743: None, 69872: None, 69873: None, 69874: None, 69875: None, 69876: None, 69877: None, 69878: None, 69879: None, 69880: None, 69881: None, 69942: None, 69943: None, 69944: None, 69945: None, 69946: None, 69947: None, 69948: None, 69949: None, 69950: None, 69951: None, 70096: None, 70097: None, 70098: None, 70099: None, 70100: None, 70101: None, 70102: None, 70103: None, 70104: None, 70105: None, 70113: None, 70114: None, 70115: None, 70116: None, 70117: None, 70118: None, 70119: None, 70120: None, 70121: None, 70122: None, 70123: None, 70124: None, 70125: None, 70126: None, 70127: None, 70128: None, 70129: None, 70130: None, 70131: None, 70132: None, 70384: None, 70385: None, 70386: None, 70387: None, 70388: None, 70389: None, 70390: None, 70391: None, 70392: None, 70393: None, 70736: None, 70737: None, 70738: None, 70739: None, 70740: None, 70741: None, 70742: None, 70743: None, 70744: None, 70745: None, 70864: None, 70865: None, 70866: None, 70867: None, 70868: None, 70869: None, 70870: None, 70871: None, 70872: None, 70873: None, 71248: None, 71249: None, 71250: None, 71251: None, 71252: None, 71253: None, 71254: None, 71255: None, 71256: None, 71257: None, 71360: None, 71361: None, 71362: None, 71363: None, 71364: None, 71365: None, 71366: None, 71367: None, 71368: None, 71369: None, 71472: None, 71473: None, 71474: None, 71475: None, 71476: None, 71477: None, 71478: None, 71479: None, 71480: None, 71481: None, 71482: None, 71483: None, 71904: None, 71905: None, 71906: None, 71907: None, 71908: None, 71909: None, 71910: None, 71911: None, 71912: None, 71913: None, 71914: None, 71915: None, 71916: None, 71917: None, 71918: None, 71919: None, 71920: None, 71921: None, 71922: None, 72784: None, 72785: None, 72786: None, 72787: None, 72788: None, 72789: None, 72790: None, 72791: None, 72792: None, 72793: None, 72794: None, 72795: None, 72796: None, 72797: None, 72798: None, 72799: None, 72800: None, 72801: None, 72802: None, 72803: None, 72804: None, 72805: None, 72806: None, 72807: None, 72808: None, 72809: None, 72810: None, 72811: None, 72812: None, 73040: None, 73041: None, 73042: None, 73043: None, 73044: None, 73045: None, 73046: None, 73047: None, 73048: None, 73049: None, 73120: None, 73121: None, 73122: None, 73123: None, 73124: None, 73125: None, 73126: None, 73127: None, 73128: None, 73129: None, 74752: None, 74753: None, 74754: None, 74755: None, 74756: None, 74757: None, 74758: None, 74759: None, 74760: None, 74761: None, 74762: None, 74763: None, 74764: None, 74765: None, 74766: None, 74767: None, 74768: None, 74769: None, 74770: None, 74771: None, 74772: None, 74773: None, 74774: None, 74775: None, 74776: None, 74777: None, 74778: None, 74779: None, 74780: None, 74781: None, 74782: None, 74783: None, 74784: None, 74785: None, 74786: None, 74787: None, 74788: None, 74789: None, 74790: None, 74791: None, 74792: None, 74793: None, 74794: None, 74795: None, 74796: None, 74797: None, 74798: None, 74799: None, 74800: None, 74801: None, 74802: None, 74803: None, 74804: None, 74805: None, 74806: None, 74807: None, 74808: None, 74809: None, 74810: None, 74811: None, 74812: None, 74813: None, 74814: None, 74815: None, 74816: None, 74817: None, 74818: None, 74819: None, 74820: None, 74821: None, 74822: None, 74823: None, 74824: None, 74825: None, 74826: None, 74827: None, 74828: None, 74829: None, 74830: None, 74831: None, 74832: None, 74833: None, 74834: None, 74835: None, 74836: None, 74837: None, 74838: None, 74839: None, 74840: None, 74841: None, 74842: None, 74843: None, 74844: None, 74845: None, 74846: None, 74847: None, 74848: None, 74849: None, 74850: None, 74851: None, 74852: None, 74853: None, 74854: None, 74855: None, 74856: None, 74857: None, 74858: None, 74859: None, 74860: None, 74861: None, 74862: None, 92768: None, 92769: None, 92770: None, 92771: None, 92772: None, 92773: None, 92774: None, 92775: None, 92776: None, 92777: None, 93008: None, 93009: None, 93010: None, 93011: None, 93012: None, 93013: None, 93014: None, 93015: None, 93016: None, 93017: None, 93019: None, 93020: None, 93021: None, 93022: None, 93023: None, 93024: None, 93025: None, 93824: None, 93825: None, 93826: None, 93827: None, 93828: None, 93829: None, 93830: None, 93831: None, 93832: None, 93833: None, 93834: None, 93835: None, 93836: None, 93837: None, 93838: None, 93839: None, 93840: None, 93841: None, 93842: None, 93843: None, 93844: None, 93845: None, 93846: None, 119520: None, 119521: None, 119522: None, 119523: None, 119524: None, 119525: None, 119526: None, 119527: None, 119528: None, 119529: None, 119530: None, 119531: None, 119532: None, 119533: None, 119534: None, 119535: None, 119536: None, 119537: None, 119538: None, 119539: None, 119648: None, 119649: None, 119650: None, 119651: None, 119652: None, 119653: None, 119654: None, 119655: None, 119656: None, 119657: None, 119658: None, 119659: None, 119660: None, 119661: None, 119662: None, 119663: None, 119664: None, 119665: None, 119666: None, 119667: None, 119668: None, 119669: None, 119670: None, 119671: None, 119672: None, 120782: None, 120783: None, 120784: None, 120785: None, 120786: None, 120787: None, 120788: None, 120789: None, 120790: None, 120791: None, 120792: None, 120793: None, 120794: None, 120795: None, 120796: None, 120797: None, 120798: None, 120799: None, 120800: None, 120801: None, 120802: None, 120803: None, 120804: None, 120805: None, 120806: None, 120807: None, 120808: None, 120809: None, 120810: None, 120811: None, 120812: None, 120813: None, 120814: None, 120815: None, 120816: None, 120817: None, 120818: None, 120819: None, 120820: None, 120821: None, 120822: None, 120823: None, 120824: None, 120825: None, 120826: None, 120827: None, 120828: None, 120829: None, 120830: None, 120831: None, 125127: None, 125128: None, 125129: None, 125130: None, 125131: None, 125132: None, 125133: None, 125134: None, 125135: None, 125264: None, 125265: None, 125266: None, 125267: None, 125268: None, 125269: None, 125270: None, 125271: None, 125272: None, 125273: None, 126065: None, 126066: None, 126067: None, 126068: None, 126069: None, 126070: None, 126071: None, 126072: None, 126073: None, 126074: None, 126075: None, 126076: None, 126077: None, 126078: None, 126079: None, 126080: None, 126081: None, 126082: None, 126083: None, 126084: None, 126085: None, 126086: None, 126087: None, 126088: None, 126089: None, 126090: None, 126091: None, 126092: None, 126093: None, 126094: None, 126095: None, 126096: None, 126097: None, 126098: None, 126099: None, 126100: None, 126101: None, 126102: None, 126103: None, 126104: None, 126105: None, 126106: None, 126107: None, 126108: None, 126109: None, 126110: None, 126111: None, 126112: None, 126113: None, 126114: None, 126115: None, 126116: None, 126117: None, 126118: None, 126119: None, 126120: None, 126121: None, 126122: None, 126123: None, 126125: None, 126126: None, 126127: None, 126129: None, 126130: None, 126131: None, 126132: None, 127232: None, 127233: None, 127234: None, 127235: None, 127236: None, 127237: None, 127238: None, 127239: None, 127240: None, 127241: None, 127242: None, 127243: None, 127244: None}
