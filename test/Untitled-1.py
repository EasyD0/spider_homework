# %%
import nltk
# from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
import pandas as pd
from collections import Counter
import numpy as np

text1 = "This paper studies unmanned aerial vehicle (UAV)-enabled wireless communication, where a rotary-wing UAV is dispatched to communicate with multiple ground nodes (GNs). We aim to minimize the total UAV energy consumption, including both propulsion energy and communication related energy, while satisfying the communication throughput requirement of each GN. To this end, we first derive a closed-form propulsion power consumption model for rotary-wing UAVs, and then formulate the energy minimization problem by jointly optimizing the UAV trajectory and communication time allocation among GNs, as well as the total mission completion time. The problem is difficult to be optimally solved, as it is non-convex and involves infinitely many variables over time. To tackle this problem, we first consider the simple fly-hover-communicate design, where the UAV successively visits a set of hovering locations and communicates with one corresponding GN while hovering at each location. For this design, we propose an efficient algorithm to optimize the hovering locations and durations, as well as the flying trajectory connecting these hovering locations, by leveraging the travelling salesman problem with neighborhood and convex optimization techniques. Next, we consider the general case, where the UAV also communicates while flying. We propose a new path discretization method to transform the original problem into a discretized equivalent with a finite number of optimization variables, for which we obtain a high-quality suboptimal solution by applying the successive convex approximation technique. The numerical results show that the proposed designs significantly outperform the benchmark schemes."
text2 = "Wireless communication involving unmanned aerial vehicles (UAVs) is expected to play an important role in future wireless networks. However, different from conventional terrestrial communication systems, UAVs typically have rather limited onboard energy on one hand, and require additional flying energy consumption on the other hand. This renders energy-efficient UAV communication with smart energy expenditure of paramount importance. In this paper, via extensive flight experiments, we aim to firstly validate the recently derived theoretical energy model for rotary-wing UAVs, and then develop a general model for those complicated flight scenarios where rigorous theoretical model derivation is quite challenging, if not impossible. Specifically, we first investigate how UAV power consumption varies with its flying speed for the simplest straight-and-level flight. With about 12,000 valid power-speed data points collected, we first apply the model-based curve fitting to obtain the modelling parameters based on the theoretical closed-form energy model in the existing literature. In addition, in order to exclude the potential bias caused by the theoretical energy model, the obtained measurement data is also trained using a model-free deep neural network. It is found that the obtained curve from both methods can match quite well with the theoretical energy model. Next, we further extend the study to arbitrary 2-dimensional (2-D) flight, where, to our best knowledge, no rigorous theoretical derivation is available for the closed-form energy model as a function of its flying speed, direction, and acceleration. To fill the gap, we first propose a heuristic energy model for these more complicated cases, and then provide experimental validation based on the measurement results for circular level flight."
text3 = "Wireless powered communication networks are promising in the next generation wireless communication systems since they can prolong the communication time of users. However, the wireless powered performance is limited due to the low energy harvesting efficiency caused by channel fading. In order to tackle this issue, rotary-wing unmanned aerial vehicle (UAV) enabled wireless powered communication network (WPCN) is first proposed to provide energy harvesting and information transmission to multiple ground users. Then, the energy consumption minimization problem for the UAV-enabled WPCN is formulated subject to the speed, initial and final positions of the UAV, the energy harvesting causality and user scheduling constraints. Finally, an efficient algorithm by employing the path discretization and successive convex approximation techniques is proposed to solve the challenging non-convex problem. Simulation results show that our proposed scheme can efficiently balance the energy harvesting phase and transmission phase based on the optimal trajectory design, moreover, it outperforms other benchmark schemes in terms of the energy consumption."
text4 = "In this letter, we study unmanned aerial vehicle (UAV) enabled Internet-of-Things (IoT) system, where a rotary-wing UAV is employed to collect data from a set of IoT devices. By introducing the propulsion energy model for rotary-wing UAV, we aim to minimize the maximum energy consumption among all devices, while satisfying the UAV energy budget. The problem is formulated with a non-convex programming by jointly optimizing the communication scheduling and transmit power allocation for devices as well as the UAV trajectory. An efficient solution is proposed by applying the alternating optimization and successive convex approximation techniques. Simulation results show that the proposed solution can achieve significant gains over benchmark schemes for data collection over IoT system."
text5 = "Unmanned aerial vehicles (UAVs) are envisioned as a promising means of providing wireless services for various complex terrains and emergency situations. In this paper, we consider a wireless UAV-enabled cognitive communication network, where a rotary-wing UAV transmits confidential information to a ground cognitive user over the spectrum assigned to primary users (PUs), while eavesdroppers attempt to wiretap the legitimate transmission. In order to enhance the secrecy performance of wireless communications, the secrecy rate (SR) of the UAV-enabled cognitive communication system is maximized through optimizing UAV three-dimensional (3D) flying trajectory while satisfying the requirements of UAV's initial and final locations and guaranteeing the constraint of maximum speed of UAV and the interference threshold of each PU. However, the formulated SR maximization (SRM) problem is non-convex. For the purpose of dealing with this intractable problem, we employ the difference of two-convex functions approximation approach to convert the non-convex optimization problem into a convex one, which is then solved through applying standard convex optimization techniques. Moreover, an iterative 3D trajectory optimization algorithm for SRM scheme is proposed to achieve the near-optimal 3D trajectory. Simulation results show that our proposed 3D trajectory optimization based SRM algorithm has good convergence, and the proposed SRM scheme outperforms the benchmark approach in terms of the SR performance."
text6 = "Accurate and convenient energy consumption models (ECMs) for rotary-wing unmanned aerial vehicles (UAVs) are important for UAV communication designs. Existing models are complex and inconvenient to use. In this letter, a simple and easy-to-use model with closed-form expression as a function of the initial velocity, acceleration and time duration is derived. Using this model, the UAV flight control parameters, such as polling force and tilt angle, are analyzed in analytical form. Numerical results show the validity and reliability of the proposed model."
text7 = "In this paper, we consider an unmanned aerial vehicle (UAV)-enabled wireless-powered communication network (WPCN), where a rotary-wing UAV is employed as a hybrid access point (AP) to serve multiple ground users (GUs). Specifically, the GUs harvest radio frequency (RF) energy from the signal sent by the UAV, which is then used by the GUs to power their uplink information transmission to the UAV. In practice, the mission completion time and energy consumption are two important indexes to evaluate the performance of UAV-enabled communication. To complete the mission as soon as possible, the UAV should fly above the ground users it serves at maximum speed, but this leads to more propulsion energy being consumed. Our objective is to reveal the energy-time tradeoff, characterized by the boundary of the so-called “Energy-Time” region. We first derive the mathematical form of the tradeoff, the UAV trajectory, user scheduling and mission completion time, as well as the time allocation, all of which need to be jointly optimized. To this end, we propose two communication protocols: (i) fly-hover-communicate and (ii) path discretization. For each protocol, we first find the two extremes, where minimum energy consumption and minimum mission completion time are achieved. We then complete the boundary for minimizing the energy consumption for given mission completion time. Moreover, because of the nonconvexity of the problem, we propose an algorithm to obtain a locally optimal solution based on the successive convex approximation (SCA) technique for both designs. Finally, the simulation results are provided to validate the effectiveness of our study."
text8 = "Rotary-wing unmanned aerial vehicles (UAVs) can be potentially used in wireless communications and therefore attract research from both academia and industry recently. However, most UAV air-to-ground channel models under 6 GHz have ignored the micro-Doppler effects due to the UAV’s propellers. In this letter, we reveal its principle and develop a method to estimate the micro-Doppler, including sounding waveform design, channel modeling, and Doppler frequency estimation. Our simulation results demonstrate that the estimated root-mean-squared error of micro-Doppler is smaller than 18.83 Hz for 963.09 Hz micro-Doppler frequency shift resulting from the rotation of the propellers in the rotary-wing UAV sub-6 GHz communications systems."
text9 = "Millimeter-wave rotary-wing (RW) unmanned aerial vehicle (UAV) air-to-ground (A2G) links face unpredictable Doppler effect arising from the inevitable wobbling of RW UAV. Moreover, the time-varying channel characteristics during transmission lead to inaccurate channel estimation, which in turn results in the deteriorated bit error probability performance of the UAV A2G link. This paper studies the impact of mechanical wobbling on the Doppler effect of the millimeter-wave wireless channel between a hovering RW UAV and a ground node. Our contributions of this paper lie in: i) modeling the wobbling process of a hovering RW UAV; ii) developing an analytical model to derive the temporal autocorrelation function (ACF) for the millimeter-wave RW UAV A2G link in a closed-form expression; and iii) investigating how RW UAV wobbling impacts the Doppler effect on the millimeter-wave RW UAV A2G link. Numerical results show that different RW UAV wobbling patterns impact the amplitude and the frequency of ACF oscillation in the millimeter-wave RW UAV A2G link. For UAV wobbling, the temporal ACF decreases quickly and the impact of the Doppler effect is significant on the millimeter-wave A2G link."
text10 = "This paper investigates the rotary-wing unmanned aerial vehicle (UAV)-enabled full-duplex wireless-powered Internet-of-Things (IoT) networks, in which a rotary-wing UAV equipped with a full-duplex hybrid access point (HAP) serves multiple sparsely-distributed energy-constrained IoT sensors. The UAV broadcasts energy when flying and hovering, and collects information only when hovering. It is assumed that the transmission range of the UAV is limited and the sensors are sparsely distributed in the IoT network. Under these practical assumptions, we formulate three optimization problems: a sum-throughput maximization (STM) problem, a total-time minimization (TTM) problem, and a total-energy minimization (TEM) problem. For the TEM problem, we further take into consideration that the power needed for hovering, flying, and transmitting are different. For the STM, TTM and TEM problems, optimal solutions are obtained. Finally, numerical results show that the performance achieved by the proposed optimal time allocation schemes outperform existing time allocation schemes. It is also observed that i) the time allocation between hovering and flying time has different trends for different goals; ii) there is an optimal UAV transmit power range that minimizes the energy consumed by the UAV during the entire cycle."
text11 = "This paper studies the three-dimensional (3D) trajectory optimization problem for unmanned aerial vehicle (UAV) aided wireless communication. Existing works mainly rely on the kinematic equations for UAV’s mobility modeling, while its dynamic equations are usually missing. As a result, the planned UAV trajectories are piece-wise line segments in general, which may be difficult to implement in practice. By leveraging the concept of state-space model, a control-based UAV trajectory design is proposed in this paper, which takes into account both of the UAV’s kinematic equations and the dynamic equations. Consequently, smooth trajectories that are amenable to practical implementation can be obtained. Moreover, the UAV’s controller design is achieved along with the trajectory optimization, where practical roll angle and pitch angle constraints are considered. Furthermore, a new energy consumption model is derived for quad-rotor UAVs, which is based on the voltage and current flows of the electric motors and thus captures both the consumed energy for motion and the energy conversion efficiency of the motors. Numerical results are provided to validate the derived energy consumption model and show the effectiveness of our proposed algorithms."
text12 = "In this paper, we study an unmanned aerial vehicle (UAV) enabled video streaming system, where a rotary-wing UAV is dispatched as a mobile base station to serve multiple ground users (GUs) with dynamic adaptive streaming over HTTP (DASH). By introducing the Quality of Experience (QoE) utility model, we investigate the joint design of transmit power and bandwidth allocation as well as UAV trajectory for maximization of minimum utility among all GUs, subject to information-causality constraints for video playing and UAV total energy budget, which consists of both communication related energy and UAV propulsion energy. The formulated problem is non-convex and difficult to be solved directly. An efficient algorithm is proposed to obtain the suboptimal solution by applying the successive convex approximation and alternating optimization techniques. Simulation results show that the proposed solution can achieve significant gains in terms of QoE utility over benchmark schemes for energy-efficient video streaming."
text13 = "This letter investigates the transmit power and trajectory optimization problem for unmanned aerial vehicle (UAV)-aided networks. Different from majority of the existing studies with fixed communication infrastructure, a dynamic scenario is considered where a flying UAV provides wireless services for multiple ground nodes simultaneously. To fully exploit the controllable channel variations provided by the UAV’s mobility, the UAV’s transmit power and trajectory are jointly optimized to maximize the minimum average throughput within a given time length. For the formulated non-convex optimization with power budget and trajectory constraints, this letter presents an efficient joint transmit power and trajectory optimization algorithm. Simulation results validate the effectiveness of the proposed algorithm and reveal that the optimized transmit power shows a water-filling characteristic in spatial domain."
text14 = "The trajectory optimization of an unpowered reentry vehicle via artificial emotion memory optimization (AEMO) is discussed. Firstly, reentry dynamics are established based on multiple constraints and parameterized control variables with finite dimensions are designed. If the constraint is not satisfied, a distance measure and an adaptive penalty function are used to address this scenario. Secondly, AEMO is introduced to solve the trajectory optimization problem. Based on the theories of biology and cognition, the trial solutions based on emotional memory are established. Three search strategies are designed for realizing the random search of trial solutions and for avoiding becoming trapped in a local minimum. The states of the trial solutions are determined according to the rules of memory enhancement and forgetting. As the iterations proceed, the trial solutions with poor quality will gradually be forgotten. Therefore, the number of trial solutions is decreased, and the convergence of the algorithm is accelerated. Finally, a numerical simulation is conducted, and the results demonstrate that the path and terminal constraints are satisfied and the method can realize satisfactory performance."
text15 = "This letter studies the optimization of a UAV-aided vehicular communication system where a rotary-wing UAV serves a moving vehicle. Considering the propulsion energy of the UAV, our goal is to maximize the energy efficiency (EE) of the system by optimizing UAV trajectory. Due to the causality of the vehicle location information (VLI), the formulated optimization problem is challenging to solve. To address the VLI causality issue, a vehicle's trajectory prediction framework is proposed, in which a short-term accurate trajectory prediction model and a long-term coarse trajectory prediction model are integrated. Based on the proposed vehicle's trajectory prediction framework, a novel receding horizon optimization method is proposed to transform the EE maximization problem into a sequence of optimization problems, in which a time window of the short-term vehicle's trajectory prediction is successively moved along the vehicle's trip. By solving the sequence of optimization problems, an energy-efficient UAV's trajectory optimization algorithm is obtained. Simulation results verify that our proposed scheme can achieve about 20%-40% EE performance gains over existing baseline schemes."
text16 = "This letter investigates fairness-aware task data allocation and trajectory optimization in unmanned aerial vehicles (UAV)-assisted mobile edge computing (MEC) systems, where a fixed-wing UAV is used as a flying computing server to receive task data of mobile terminals (MTs). Under the fairness consideration, we aim to minimize the maximum energy consumption among all MTs. Despite the non-convexity of the original formulated joint optimization problem, we transform the problem into two convex sub-problems by introducing auxiliary variables, and solve them jointly by proposing an iterative algorithm. Simulation results show that the proposed algorithm can effectively reduce the maximum energy consumption among all MTs."
text17 = "In this brief, we presented a framework for the trajectory optimization of the 5-link Biped Robot using the Beetle Antennae Search (BAS) algorithm. The biped robot is highly non-linear and has complex dynamical modeling. It is challenging to obtain a closed-form solution for the Robot. The robot modeling has two stages, i.e., the optimal trajectory generation and the robust control of a robot. The conventional methodologies treat both problems separately and are computationally expensive. This brief presented an optimization problem that combines the trajectory generation and control problem of a 5-link biped robot. We employed Beetle Antennae Search (BAS) for the problem’s online-solution, an intelligent online optimization approach. BAS is a single-particle searching algorithm, which makes it robust, computationally, and memory-wise efficient. We applied BAS on two non-linear systems, i.e., inverted pendulum and 5-link biped robot, and convincing results are obtained with BAS."
text18 = "In this letter, we consider a cooperative Internet of unmanned aerial vehicles (UAVs) in which the UAV collects data from ground sensors (GSs) and transmits the received data to the base station (BS) for further processing. The data at the UAV can either be transmitted directly to the BS via the cellular mode or be transmitted through the other UAV via the relay mode. The objective is to minimize the completion time for all the tasks by joint mode selection and trajectory optimization, which can be decoupled into a series of convex optimization problems. The simulation results show that the relay mode is more likely to be selected when the signal-to-noise ratio (SNR) threshold is higher than 10 dB. Otherwise, the UAV prefers to transmit in the cellular mode."
text19 = "In this letter, we study the resource allocation and trajectory optimization for multi-UAV based wireless networks. Our design maximizes the number of admitted users while satisfying their data transmission demands, which formulates a mixed-integer nonlinear problem. To tackle its difficulty, we first introduce soft admission variables and propose an iterative algorithm to solve this admission maximization problem. Each iteration comprises two steps, namely soft admission maximization and user removal. Our method guarantees that the number of admitted users increases over iterations. Numerical results show that our algorithm outperforms the conventional approach based on block coordinate ascent and mixed-integer linear programming."
text20 = "This article investigates an unmanned aerial vehicle (UAV)-enabled wireless communication network with multiple pairs of source-destination ground users (GUs), where the rotary-wing UAV acts as an aerial mobile relay to transfer information from the source GUs to corresponding destination GUs when the direct terrestrial communication is blocked. On the premise of satisfying the communication requirements of all GUs, we intend to minimize the total energy consumption of supporting the propulsion and communication by jointly optimizing communication time, UAV transmit power allocation and UAV trajectory. To tackle the formulated non-convex problem, we first transform the original problem into a more tractable form with a finite number of optimization variables using the path discretization approach. Then, we decompose the joint optimization problem into three subproblems to find a near optimal solution. Finally, these subproblems can be efficiently solved via the proposed iterative algorithm based on block coordinate descent and successive convex approximation (SCA) techniques. As the initial UAV trajectory has significant influence on the final results, we put forward a novel trajectory initialization scheme by combining the classic Pickup-and-Delivery Problem with fly-hover-communication protocol. Numerical results demonstrate that our proposed design contributes to significant performance enhancement compared with other two benchmarks."
text21 = "The convergence of artificial intelligence (AI) and the Internet of Things (IoT) promotes energy-efficient communication in smart homes. Quality-of-Service (QoS) optimization during video streaming through wireless micro medical devices (WMMDs) in smart healthcare homes is the main purpose of this research. This article contributes in four distinct ways. First, to propose a novel lazy video transmission algorithm (LVTA). Second, a novel video transmission rate control algorithm (VTRCA) is proposed. Third, a novel cloud-based video transmission framework is developed. Fourth, the relationship between buffer size and performance indicators, i.e., peak-to-mean ratio (PMR), energy (i.e., encoding and transmission), and standard deviation, is investigated while comparing LVTA, VTRCA, and baseline approaches. The experimental results demonstrate that the reduction in encoding (32% and 35.4%) and transmission (37% and 39%) energy drains, PMR (5 and 4), and standard deviation (3 and 4 dB) for VTRCA and LVTA, respectively, is greater than that obtained by baseline during video streaming through WMMD."
text22 = "In this letter, we consider a UAV flying over multiple locations and serves as many users as possible within a given time duration. We study the problem of optimal trajectory design, which we formulate as a mixed-integer linear program. For large instances of the problem where the options for trajectories become prohibitively many, we establish a connection to the orienteering problem, and propose a corresponding greedy algorithm. Simulation results show that the proposed algorithm is fast and yields solutions close to the optimal ones. The proposed algorithm can be used for trajectory planning in content caching or tactical field operations."
text23 = "Conventional adaptive modulation (AM) scheme achieves capacity gain by adapting its modulation index with the wireless channel state. The channel state information (CSI) is learned from the receiver feedback in every time slot, which wastes energy. In this letter, we propose to exploit temporally correlated dynamic wireless channel state to compute CSI-dependent interval between successive feedbacks and to select an appropriate modulation index in AM-based transmission. Our analysis and numerical results demonstrate that the proposed dynamic feedback-based AM offers about 22% or higher energy efficiency along with 13% or higher data throughput over its nearest competitive approach in a nominal mobility range."
text24 = "This letter proposes a generalised propulsion energy consumption model (PECM) for rotary-wing unmanned aerial vehicles (UAVs) under the consideration of the practical thrust-to-weight ratio (TWR) with respect to the velocity, acceleration and direction change of the UAVs. To verify the effectiveness of the proposed PECM, we consider a UAV-enabled communication system, where a rotary-wing UAV serves multiple ground users as an aerial base station. We aim to maximize the energy efficiency (EE) of the UAV by jointly optimizing the user scheduling and UAV trajectory variables. However, the formulated problem is a non-convex fractional integer programming problem, which is challenging to obtain its optimal solution. To tackle this problem, we propose an efficient iterative algorithm by decomposing the original problem into two sub-problems to obtain a suboptimal solution based on the successive convex approximation technique. Simulation results show that the optimized UAV trajectory by applying the proposed PECM are smoother and the corresponding EE has significant improvement as compared to other benchmark schemes."
text25 = "In this paper, a method based on the successive convexification is proposed to solve the ascent trajectory optimization problem, the algorithm converges to the optimal solution quickly even if the initial guess is coarse. A three-dimensional motion is formulated with complex aerodynamics and terminal constraints. Based on the modified aerodynamic coefficients, the new auxiliary control variables are designed to deal with the complex aerodynamics and non-smooth of control variables in the discrete optimization problem. The inner nonconvex constraints between the new control are relaxed to be convex without loss. The artificial infeasibility and unboundedness caused by linearization are tackled by the virtual controls and soft constraint for trust region in the successive convexification. The good convergence of the proposed method is illustrated by the iterative solutions of the ascent trajectory optimization problem for a small guided rocket, the accuracy is verified by the comparison with the optimal solution given by the typical optimal control solvers, and the feasibility and stability are demonstrated by optimal solutions of the ascent trajectory optimization problems under different missions and dispersed conditions. These excellent performances validated by the adequate simulations indicate that the proposed algorithm can be implemented online."

main_abstract = text1
sim_abstract_list = [text1, text2, text3, text4, text5, text6, text7, text8, text9, text10, text11, text12, text13,
                     text14, text15, text16, text17, text18, text19, text20, text21, text22, text23, text24, text25]

print([main_abstract, *sim_abstract_list])


# %%
def get_wordnet_pos(treebank_tag):  # 词性转化成 WordNetLemmatizer 可识别的
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN


def rm_verb_adv(text=''):
    lemmatizer = WordNetLemmatizer()
    taged_word_list = nltk.pos_tag(text.lower().split())
    # return [lemmatizer.lemmatize(token, get_wordnet_pos(tag)) for token, tag in taged_word_list if not (tag.startswith('R') or tag.startswith('V') or tag =='IN' or tag=='PRP' or tag =='DT' or tag=='CC')]

    return [lemmatizer.lemmatize(token, get_wordnet_pos(tag)) for token, tag in taged_word_list if
            not (tag.startswith('R') or tag == 'IN' or tag == 'PRP' or tag == 'DT' or tag == 'CC')]


# %%
dataset = pd.DataFrame({'abs_list': [*sim_abstract_list, main_abstract]})  # 合成pandas
dataset['abs_list'] = dataset['abs_list'].str.replace(r"[^\w’]+", ' ', regex=True)  # 删除标点

# 删除动词和副词
dataset['abs_list'] = dataset['abs_list'].apply(rm_verb_adv)
print(text2)
print(dataset['abs_list'][0])
dataset.head()

# %%
# 制作单词表
all_words = dataset['abs_list'].sum() + dataset['abs_list'][len(dataset) - 1] * 20
word_counts = Counter(all_words)
word_pd = pd.DataFrame(word_counts.items(), columns=['word', 'count'])
word_pd = word_pd.sort_values('count', ascending=False).reset_index(drop=True)
word_pd.head()

# %%

q1 = word_pd['count'].quantile(0.4)
q2 = word_pd['count'].quantile(0.99)
word_pd_80 = word_pd[(word_pd['count'] >= q1) & (word_pd['count'] <= q2)].reset_index(drop=True)
word_pd_80.head(3)
word_pd_80.info()

# word_pd_80=word_pd

# 计算idf
article_num = len(dataset)
df_temp = dataset['abs_list'].apply(lambda x: word_pd_80['word'].isin(x).astype(int)).sum()
idf = np.log(article_num / df_temp)  # 计算idf
Idf_Dict = dict(zip(word_pd_80['word'], idf))
# print(Idf_Dict)
Idf = pd.DataFrame(list(Idf_Dict.items()), columns=['word', 'idf'])
Idf.head()


# %%
class tfidf:
    Idf = pd.DataFrame(columns=['word', 'idf'])

    def __init__(self, Idf):
        self.Idf = Idf

    def get_tf(self, wd_list):
        word_count = Counter(wd_list)
        df = pd.DataFrame(columns=['word', 'frequency'])

        # 遍历词汇表中的每个单词
        # for i, word in list(Idf.loc[:,'word']):
        for i, word in enumerate(self.Idf['word'].tolist()):
            # 如果单词在 word_list 中出现过，则将其添加到 DataFrame 中
            if word in word_count:
                df.loc[i] = [word, word_count[word]]
            else:
                df.loc[i] = [word, 0]
        df['frequency'] /= len(wd_list)
        return df

    def get_tfidf(self, wd_list):
        tf = self.get_tf(wd_list)

        return np.array(self.Idf['idf'] * tf['frequency'])


# %%
mytfidf = tfidf(Idf)
dataset['tfidf_vec'] = dataset['abs_list'].apply(mytfidf.get_tfidf)
dataset.head()

# %%
cosine_similarity(dataset['tfidf_vec'][0].reshape(1, -1), dataset['tfidf_vec'][3].reshape(1, -1))

# %%
end_index = len(dataset) - 1
score_list = [np.dot(dataset['tfidf_vec'][i], dataset['tfidf_vec'][end_index]) / (
            np.linalg.norm(dataset['tfidf_vec'][i]) * np.linalg.norm(dataset['tfidf_vec'][end_index])) for i in
              range(end_index)]

print(score_list)

# %% [markdown]
# 

# %%
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 将文本存储在列表中
texts = [main_abstract, *sim_abstract_list]

# 创建TF-IDF向量化器
tfidf_vectorizer = TfidfVectorizer()

# 计算每篇文章和text1的TF-IDF向量
tfidf_vectors = tfidf_vectorizer.fit_transform(texts)

# 计算每篇文章和text1的相似度
text1_similarities = cosine_similarity(tfidf_vectors[0], tfidf_vectors[1:]).flatten()

# 输出每篇文章和text1的相似度
for i, similarity in enumerate(text1_similarities):
    print(f"相似度( text{i + 2}): {similarity:.4f}")