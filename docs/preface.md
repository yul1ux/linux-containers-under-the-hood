# Preface

Docker (သို့) Podman နဲ့ container တစ်ခု run ရတာ မခက်ပါဘူး။ Command ကို သိရင် application ကို စတင်နိုင်ပါတယ်။ ဒါပေမဲ့ container run နေတဲ့အချိန်မှာ အောက်ခံမှာ ဘာတွေဖြစ်နေလဲဆိုတာကိုတော့ command သိရုံနဲ့ မရှင်းပြနိုင်ပါဘူး။

ဥပမာ -

- Container ထဲက process တွေကို Linux က ဘယ်လိုခွဲခြားထားသလဲ။
- Container တစ်ခုက ကိုယ့် filesystem ကိုပဲ မြင်ရတာ ဘာကြောင့်လဲ။
- Memory limit သတ်မှတ်လိုက်တဲ့အခါ kernel က ဘယ်လိုထိန်းချုပ်သလဲ။
- Image တစ်ခုကို run လုပ်တဲ့အခါ runtime က ဘာတွေ ပြင်ဆင်ပေးရသလဲ။

ဒီမေးခွန်းတွေကို ဖြေဖို့ container ကို သုံးနည်းတင်မကဘဲ အလုပ်လုပ်ပုံကိုပါ နားလည်ဖို့ လိုပါတယ်။ ဒီစာအုပ်က Linux container နည်းပညာရဲ့ အတွင်းပိုင်းကို မြန်မာဘာသာနဲ့ အခြေခံကနေ စပြီး တစ်ဆင့်ချင်း ရှင်းပြဖို့ ရေးထားတာပါ။ Container ကို command တစ်ခု (သို့) image file တစ်ခုအဖြစ်ပဲ မကြည့်ဘဲ Linux kernel က စီမံပေးနေတဲ့ process တွေ၊ သူတို့ မြင်ရတဲ့ resource တွေနဲ့ runtime က ပြင်ဆင်ပေးတဲ့ execution environment တစ်ခုအဖြစ် ကြည့်သွားပါမယ်။

## ဘယ်သူတွေ ဖတ်လို့ရမလဲ

Linux နဲ့ container နည်းပညာကို ပိုနားလည်ချင်သူတွေအတွက် ရည်ရွယ်ထားပါတယ်။

- Linux ကို စတင်လေ့လာနေပြီး process နဲ့ kernel အလုပ်လုပ်ပုံကို ပိုသိချင်သူများ။
- Docker၊ Podman (သို့) တခြား container tool တွေကို နေ့စဉ်သုံးနေပေမဲ့ နောက်ကွယ်က mechanism ကို သိချင်သူများ။
- System administration၊ DevOps၊ Site Reliability Engineering (SRE) နဲ့ platform engineering နယ်ပယ်မှာ လုပ်ကိုင်နေသူများ။

Docker၊ Podman၊ Kubernetes (သို့) OCI specification ကို ကြိုသိထားဖို့ မလိုပါဘူး။ Linux terminal ကို အခြေခံသုံးဖူးပြီး file၊ directory၊ process ကို အကြမ်းဖျင်း သိရင် စဖတ်လို့ရပါတယ်။ ဘယ်လောက်အထိ ကြိုသိထားသင့်လဲဆိုတာကို [Before You Begin](before-you-begin.md) မှာ ပိုရှင်းပြထားပါတယ်။

## ဒီစာအုပ်က ဘာကို အာရုံစိုက်သလဲ

အဓိကအာရုံစိုက်ရာက **Linux OS-level container** တွေနဲ့ အဲဒီ container တွေကို ဖြစ်လာစေတဲ့ kernel နဲ့ userspace mechanism တွေပါ။ ဒါကြောင့် -

- Docker၊ Podman၊ Kubernetes ကို သုံးနည်း command reference စာအုပ် မဟုတ်ပါဘူး။ Tool တွေကို နားလည်ဖို့ လိုတဲ့ အတိုင်းအတာအထိပဲ မိတ်ဆက်ပါတယ်။
- Linux kernel source code ကို အကုန် ခွဲခြမ်းစိတ်ဖြာတဲ့ စာအုပ် မဟုတ်ပါဘူး။ Kernel feature တွေကို container ကို နားလည်ဖို့ လိုတဲ့ အတိုင်းအတာအထိ ရှင်းပြပါတယ်။

## ဖတ်ရင်း ဘယ်လိုတိုးတက်သွားမလဲ

ပထမဆုံး container ဆိုတာ ဘာလဲ၊ process နဲ့ system call က ဘာဖြစ်လို့ အရေးကြီးလဲဆိုတာကနေ စပါမယ် (Part I)။ ပြီးရင် Linux kernel က process တစ်ခုကို ဘယ်လို ခွဲခြားပြီး ကန့်သတ်ပေးသလဲ — namespace၊ cgroup၊ capability နဲ့ filesystem isolation — ကို ကြည့်ပါမယ် (Part II)။ အဲဒီအခြေခံပေါ်မှာ image storage နဲ့ networking (Part III)၊ OCI specification နဲ့ `runc`၊ `containerd`၊ Docker Engine လို runtime တွေ (Part IV)၊ security နဲ့ လည်ပတ်ရေး (Part V) ကို ဆက်သွားပြီး နောက်ဆုံးမှာ Podman၊ Kubernetes နဲ့ ကိုယ်ပိုင် runtime တစ်ခု တည်ဆောက်ခြင်း (Part VI) အထိ ရောက်မှာပါ။ Part တစ်ခုချင်းစီရဲ့ အကျဉ်းကို [Home](index.md) မှာ ကြည့်နိုင်ပါတယ်။

## ရှင်းပြပုံ

အကြောင်းအရာတစ်ခုကို အရင်ဆုံး ဘာကြောင့် လိုအပ်လာသလဲဆိုတဲ့ ပြဿနာကနေ စပါမယ်။ ပြီးရင် ဥပမာနဲ့ စိတ်ကူးကြည့်ပြီး အဓိပ္ပာယ်၊ အလုပ်လုပ်ပုံနဲ့ တခြား mechanism တွေနဲ့ ဆက်စပ်ပုံကို ရှင်းပြပါမယ်။ Table၊ diagram၊ command နဲ့ code snippet တွေကို လိုအပ်တဲ့နေရာမှာ သုံးထားပါတယ်။

တစ်ခု သတိထားစရာ ရှိပါတယ်။ **Linux kernel ရဲ့ behavior**၊ **specification (OCI စတာ) က သတ်မှတ်ထားတာ** နဲ့ **Docker၊ Podman၊ runtime တစ်ခုချင်းစီရဲ့ implementation** ဟာ အမြဲတူတာ မဟုတ်ပါဘူး။ Version အလိုက် ကွာနိုင်တာတွေလည်း ရှိပါတယ်။ ဒါကြောင့် "အမြဲမှန်တယ်" လို့ မရေးဘဲ ဘယ်အခြေအနေမှာ မှန်သလဲ၊ ဘယ်အချက်က ဘယ်အဆင့်ရဲ့ အချက်လဲဆိုတာကို ခွဲပြီး ဖော်ပြထားပါတယ်။ Technical claim တွေကို သက်ဆိုင်ရာ manual၊ kernel documentation၊ specification (သို့) product documentation နဲ့ ချိတ်ထားပါတယ်။

Command၊ system call၊ API၊ file path နဲ့ specification အမည်တွေကို ရှာဖွေရလွယ်အောင် မူရင်း English အတိုင်း ထားပါတယ်။ စာအုပ်ထဲက ပုံစံတွေကို ဘယ်လိုဖတ်ရမလဲဆိုတာကို [Before You Begin](before-you-begin.md) မှာ ရှင်းပြထားပါတယ်။

## Lab တွေအကြောင်း

Lab တွေက ဖတ်ထားတဲ့ concept ကို ကိုယ်တိုင်ကြည့်ပြီး နားလည်စေဖို့ ရည်ရွယ်ပါတယ်။ ဒါပေမဲ့ **Lab instruction ရှိတာနဲ့ စမ်းသပ်ပြီးပြီလို့ မယူဆပါနဲ့။** စမ်းသပ်ပြီး/မပြီး status ကို Lab တစ်ခုချင်းစီမှာ ဖော်ပြထားပါတယ်။ Privilege လိုတဲ့ command၊ host setting ပြောင်းတဲ့အလုပ် (သို့) production system ပေါ်က စမ်းသပ်မှုတွေကို ခွင့်ပြုချက်မရှိဘဲ မလုပ်ပါနဲ့။ Lab မလုပ်နိုင်သေးရင်လည်း အခန်းရဲ့ explanation နဲ့ diagram တွေကို ဆက်ဖတ်နိုင်ပါတယ်။

## စာဖတ်သူအတွက်

ဒီစာအုပ်ကို အစကနေ အဆုံးထိ တစ်ခါတည်း ဖတ်ဖို့ မလိုပါဘူး။ ဒါပေမဲ့ အခန်းတွေကို အစဉ်လိုက် ဖတ်ရင် အကြောင်းအရာတွေ ပိုဆက်စပ်နားလည်နိုင်ပါတယ်။ တစ်ခုခု မရှင်းရင် အဲဒီအခန်းရဲ့ diagram၊ ဥပမာနဲ့ reference ကို ပြန်ကြည့်ပါ။ Technical term တစ်ခုကို နားလည်သွားတာထက် အဲဒါက ဘာပြဿနာကို ဖြေရှင်းပေးတာလဲ၊ ဘာတွေကို မဖြေရှင်းပေးနိုင်ဘူးလဲဆိုတာကိုပါ စဉ်းစားကြည့်ပါ။

Container တစ်ခုကို run တတ်တာက စတင်ခြင်းပါ။ ဘာကြောင့် အဲဒီလို run နေသလဲဆိုတာကို ရှင်းပြနိုင်လာတာက ဒီစာအုပ်က ကူညီချင်တဲ့ နောက်တစ်ဆင့် ဖြစ်ပါတယ်။
