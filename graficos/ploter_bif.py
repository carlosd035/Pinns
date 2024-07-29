## -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

results = np.load("results_bif.npy" , allow_pickle=True).item()

T_f = results["Time_f"]
t = results["Time_t"]
T_plot= t


p_pred1 = np.load("p_predicted_vessel1.npy", allow_pickle=True)
p_pred2 = np.load("p_predicted_vessel2.npy", allow_pickle=True)
p_pred3 = np.load("p_predicted_vessel3.npy", allow_pickle=True)
p_test1 = results["TestPress_1"]/133.33
p_test2 = results["TestPress_2"]/133.33
p_test3 = results["TestPress_3"]/133.33
u_pred1 = np.load("U_predicted_vessel1.npy", allow_pickle=True)
u_pred2 = np.load("U_predicted_vessel2.npy", allow_pickle=True)
u_pred3 = np.load("U_predicted_vessel3.npy", allow_pickle=True)
u_test1 = results["TestVel_1"]
u_test2 = results["TestVel_2"]
u_test3 = results["TestVel_3"]

fig1 = plt.figure(1,figsize=(15, 10), dpi=300, facecolor='w', frameon = False)
fig2 = plt.figure(2,figsize=(15, 10), dpi=300, facecolor='w', frameon = False)
fig3 = plt.figure(3,figsize=(15, 10), dpi=300, facecolor='w', frameon = False)
fig4 = plt.figure(4,figsize=(15, 10), dpi=300, facecolor='w', frameon = False)
fig5 = plt.figure(5,figsize=(15, 10), dpi=300, facecolor='w', frameon = False)
fig6 = plt.figure(6,figsize=(15, 10), dpi=300, facecolor='w', frameon = False)

fig1.clf()
fig2.clf()
fig3.clf()
fig4.clf()
fig5.clf()
fig6.clf()

ax1 = fig1.add_subplot(111)  
ax2 = fig2.add_subplot(111)  
ax3 = fig3.add_subplot(111)  
ax4 = fig4.add_subplot(111)   
ax5 = fig5.add_subplot(111)   
ax6 = fig6.add_subplot(111)  

ax1.plot(t, u_test1,'r-',linewidth=2, markersize=0.5, label='Reference Velocity Vessel 1')

ax1.plot(T_plot, u_pred1,'b--',linewidth=2, markersize=0.5, label='Predicted Velocity Vessel 1')
ax1.set_xlabel('$t$',fontsize=10)
ax1.set_ylabel('$u(x = 0.08)$',fontsize=10)
ax1.tick_params(axis='both',grid_linewidth = 40, which='major', labelsize=35)
ax2.plot(t, u_test2,'r-',linewidth=2, markersize=0.5, label='Reference Velocity Vessel 2')

ax2.plot(T_plot, u_pred2,'b--',linewidth=2, markersize=0.5, label='Predicted Velocity Vessel 2')
ax2.set_xlabel('$t$',fontsize=10)
ax2.set_ylabel('$u(x = 0.1736)$',fontsize=10)
ax2.tick_params(axis='both', which='major', labelsize=10)
ax3.plot(t, u_test3,'r-',linewidth=2, markersize=0.5, label='Reference Velocity Vessel 3')

ax3.plot(T_plot, u_pred3,'b--',linewidth=2, markersize=0.5, label='Predicted Velocity Vessel 3')
ax3.set_xlabel('$t$',fontsize=10)
ax3.set_ylabel('$u(x = 0.1738)$',fontsize=10)
ax3.tick_params(axis='both', which='major', labelsize=10)


ax4.plot(t, p_test1,'r-',linewidth=2, markersize=0.5, label='Reference Pressure Vessel 1')
ax4.plot(T_plot, p_pred1,'b--',linewidth=2, markersize=0.5, label='Predicted Pressure Vessel 1')
ax4.set_xlabel('$t$',fontsize=10)
ax4.set_ylabel('$p(x = 0.08)$',fontsize=10)
ax4.tick_params(axis='both', which='major', labelsize=10)

ax5.plot(t, p_test2,'r-',linewidth=2, markersize=0.5, label='Reference Pressure Vessel 2')
ax5.plot(T_plot, p_pred2,'b--',linewidth=2, markersize=0.5, label='Predicted Pressure Vessel 2')
ax5.set_xlabel('$t$',fontsize=10)
ax5.set_ylabel('$p(x = 0.1736)$',fontsize=10)
ax5.tick_params(axis='both', which='major', labelsize=10)

ax6.plot(t, p_test3,'r-',linewidth=2, markersize=0.5, label='Reference Pressure Vessel 3')
ax6.plot(T_plot, p_pred3,'b--',linewidth=2, markersize=0.5, label='Predicted Pressure Vessel 3')
ax6.set_xlabel('$t$',fontsize=10)
ax6.set_ylabel('$p(x = 0.1738)$',fontsize=10)
ax6.tick_params(axis='both', which='major', labelsize=10)
   
ax1.legend(loc='upper right', frameon=False, prop={'size': 10})
ax2.legend(loc='upper right', frameon=False, prop={'size': 10})
ax3.legend(loc='upper right', frameon=False, prop={'size': 10})
ax4.legend(loc='upper right', frameon=False, prop={'size': 10})
ax5.legend(loc='upper right', frameon=False, prop={'size': 10})
ax6.legend(loc='upper right', frameon=False, prop={'size': 10})

ax1.set_ylim(-0.5,4.1)   
ax2.set_ylim(-0.5,5.1)
ax3.set_ylim(-0.5,3.5)
ax4.set_ylim(0,1100)   
ax5.set_ylim(0,1100)
ax6.set_ylim(0,1100)


filename1 = "comparative_velocity1.png"
filename2 = "comparative_velocity2.png"
filename3 = "comparative_velocity3.png"
filename4 = "comparative_pressure1.png"
filename5 = "comparative_pressure2.png"
filename6 = "comparative_pressure3.png"

fig1.savefig(filename1, format = 'png')
fig2.savefig(filename2, format = 'png')    
fig3.savefig(filename3, format = 'png')
fig4.savefig(filename4, format = 'png')    
fig5.savefig(filename5, format = 'png')
fig6.savefig(filename6, format = 'png')


