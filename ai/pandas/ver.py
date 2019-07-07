from __future__ import print_function

import pandas as pd
print(pd.__version__)


def get_mymatrics(validation_targets,validation_probabilities,thold):
  th = thold
  x_real = np.array(validation_targets)
  x_prob = np.array(validation_probabilities).reshape(-1,1)
  x_ok = np.concatenate([x_real, x_prob], axis = 1)
  df_ok = pd.DataFrame(x_ok,columns=['x_real','x_prob'])

  def get_name(a,b,th):
    ret='null'
    if (a==1):
      if (b<th):
        ret = 'FN'
      else:
        ret = 'TP'
    else:
      if (b<th):
        ret = 'TN'
      else:
        ret = 'FP'    
    return ret

  df_ok['tag'] = df_ok.apply(lambda x: get_name(x.x_real, x.x_prob,th), axis = 1)
  dd = df_ok.groupby('tag').count()
  dtp = dd.at['TP','x_real']
  dfp = dd.at['FP','x_real']
  dfn = dd.at['FN','x_real']
  dtn = dd.at['TN','x_real']
  # 正确率（精度）,查准率，查全率，假正率
  p_accuracy = format(float(dtp+dtn)/float(dtp+dfp+dfn+dtn),'.2f')
  p_precision = format(float(dtp)/float(dtp+dfp),'.2f')
  p_recall = format(float(dtp)/float(dtp+dfn),'.2f')
  p_fpr = format(float(dfp)/float(dtn+dfp),'.2f')

  print("概率值为 %0.2f 表现如下：" %th)
  print("  TP : %04d     FP : %04d" % (dtp, dfp))
  print("  FN : %04d     TN : %04d" % (dfn, dtn))
  print("精度  （Accuracy）  ：" , p_accuracy)
  print("查准率（Precision） ：" , p_precision)
  print("查全率（Recall）    ：" , p_recall)
  print("假正率（FPR）       ：" , p_fpr)
  

